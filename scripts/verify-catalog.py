#!/usr/bin/env python3
"""Verify original upstream URLs, fork provenance, gitlinks and initialized checkouts."""
from pathlib import Path, PurePosixPath
import argparse
import configparser
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=True).stdout


def verify(metadata_only=False):
    catalog = json.loads((ROOT / "catalog.json").read_text())
    projects = catalog["projects"]
    assert len(projects) == catalog["projectCount"]
    modules = configparser.RawConfigParser()
    modules.read(ROOT / ".gitmodules")
    paths, upstreams, forks, ids = set(), set(), set(), set()
    assert len(modules.sections()) == len(projects)
    gitlinks = {}
    for record in git("ls-files", "--stage", "-z").split(b"\0"):
        if not record:
            continue
        meta, name = record.split(b"\t", 1)
        mode, commit, stage = meta.decode().split()
        assert stage == "0", "Unmerged index entry"
        if mode == "160000":
            gitlinks[name.decode()] = commit
    initialized = 0
    for project in projects:
        path, upstream, fork = project["path"], project["upstream"], project["fork"]
        assert re.fullmatch(r"games/[A-Za-z0-9_./-]+", path) and ".." not in PurePosixPath(path).parts
        assert path not in paths and upstream not in upstreams and fork not in forks
        assert project["forkRepositoryId"] not in ids
        paths.add(path)
        upstreams.add(upstream)
        forks.add(fork)
        ids.add(project["forkRepositoryId"])
        assert fork.startswith("plemulabs/") and not upstream.lower().startswith("plemulabs/")
        assert project["forkParentRepositoryId"] == project["upstreamRepositoryId"]
        section = modules['submodule "' + path + '"']
        assert section["path"] == path
        assert section["url"] == "https://github.com/" + upstream + ".git"
        assert section.get("shallow") == "true"
        commit = project["commit"]
        assert re.fullmatch(r"[0-9a-f]{40}", commit) and gitlinks.get(path) == commit
        if metadata_only:
            continue
        assert (ROOT / path / ".git").exists(), "Initialize submodule: " + path
        assert git("-C", path, "rev-parse", "HEAD").decode().strip() == commit
        assert git("-C", path, "remote", "get-url", "origin").decode().strip() == section["url"]
        assert not git("-C", path, "status", "--porcelain", "--untracked-files=no"), "Changed source: " + path
        initialized += 1
    assert set(gitlinks) == paths
    roster = (ROOT / "docs/decomp-roster.md").read_bytes()
    assert hashlib.sha256(roster).hexdigest() == catalog["sourceRoster"]["sha256"]
    references = set(re.findall(r"https://github.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", roster.decode()))
    assert references == upstreams, "Every repository in the source roster must be represented"
    return {"result": "passed", "projects": len(projects), "originalUpstreamUrls": len(paths),
            "distinctOrganizationForks": len(forks), "pinnedGitlinks": len(gitlinks),
            "verifiedInitializedCheckouts": initialized, "buildsOrGamesTested": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metadata-only", action="store_true", help="Check the catalog/index without requiring initialized submodules")
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.metadata_only), indent=2))
    except (AssertionError, KeyError, ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit("Catalog verification failed: " + str(error))
