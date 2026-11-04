# Retro Decomps

51 classic-game decompilation, disassembly and native-reconstruction repositories from the [Plemu source roster](https://github.com/plemulabs/plemu-skr/blob/main/decomp-roster.md).

Every project was forked into [PlemuLabs](https://github.com/plemulabs) before registration here. **All submodule URLs point to the original upstream repositories**, and every checkout is pinned to a specific commit. The organization forks are linked separately for future development. GitHub account used for setup: `0xbae`.

## Get the sources

```sh
git clone git@github.com:0xbae/retro-decomps.git
cd retro-decomps
git submodule update --init --depth 1 --jobs 4
python3 scripts/verify-catalog.py
```

Top-level game checkouts are shallow. Fetch history inside an individual project when needed with `git fetch --unshallow`. Nested upstream dependencies are not initialized automatically; follow each project's build instructions when selecting a game to work on.

This collection does not run upstream setup scripts, compile games, extract assets or fetch separate ROM/BIOS/release downloads. A checked-out repository is not a tested build. Each project retains its original authorship and licensing; the catalog does not relicense its contents. GitHub license detection in the machine-readable manifest is informational and can be incomplete.

The SNES native-reconstruction group produces host applications rather than SNES ROMs. N64 projects are included for research and are outside Plemu's current emulator coverage. [Historical build and modding notes](docs/decomp-roster.md) retain their original verification date.

## Catalog

The 50 primary projects and the earlier `StanHash/fe6` reference are all included. FE6's current continuation and older reference each have their own original submodule and separate PlemuLabs fork.

### NES (1)

| Game | Original source | PlemuLabs fork | Pinned commit |
| --- | --- | --- | --- |
| Super Mario Bros. | [Xkeeper0/smb1](https://github.com/Xkeeper0/smb1) | [plemulabs/smb1](https://github.com/plemulabs/smb1) | [1cc3c92c](https://github.com/Xkeeper0/smb1/commit/1cc3c92cbbe8cda44903657f3da332688e806a89) |

### GB (2)

| Game | Original source | PlemuLabs fork | Pinned commit |
| --- | --- | --- | --- |
| Pokémon Red / Blue | [pret/pokered](https://github.com/pret/pokered) | [plemulabs/pokered](https://github.com/plemulabs/pokered) | [0dbf95cd](https://github.com/pret/pokered/commit/0dbf95cd12f5b1511c62ce69efe283000f780a8f) |
| Pokémon Yellow | [pret/pokeyellow](https://github.com/pret/pokeyellow) | [plemulabs/pokeyellow](https://github.com/plemulabs/pokeyellow) | [b452f2ab](https://github.com/pret/pokeyellow/commit/b452f2ab07185075140061c5084ab866d5e4a794) |

### GBC (2)

| Game | Original source | PlemuLabs fork | Pinned commit |
| --- | --- | --- | --- |
| Pokémon Crystal | [pret/pokecrystal](https://github.com/pret/pokecrystal) | [plemulabs/pokecrystal](https://github.com/plemulabs/pokecrystal) | [3c813b0b](https://github.com/pret/pokecrystal/commit/3c813b0b4d82b39bf62185aceffb76fd6026c70b) |
| The Legend of Zelda: Link's Awakening DX | [zladx/LADX-Disassembly](https://github.com/zladx/LADX-Disassembly) | [plemulabs/LADX-Disassembly](https://github.com/plemulabs/LADX-Disassembly) | [2a5c2c0d](https://github.com/zladx/LADX-Disassembly/commit/2a5c2c0d6df93a54df81ae9e1fe28b5c2fd60d03) |

### GBA (23)

| Game | Original source | PlemuLabs fork | Pinned commit |
| --- | --- | --- | --- |
| Pokémon Emerald | [pret/pokeemerald](https://github.com/pret/pokeemerald) | [plemulabs/pokeemerald](https://github.com/plemulabs/pokeemerald) | [731ad5bf](https://github.com/pret/pokeemerald/commit/731ad5bfd6e6f265508d0efcca0ba42f9dcf5881) |
| Pokémon FireRed / LeafGreen | [pret/pokefirered](https://github.com/pret/pokefirered) | [plemulabs/pokefirered](https://github.com/plemulabs/pokefirered) | [ce6406d8](https://github.com/pret/pokefirered/commit/ce6406d8c2eaf46d543c8a2606de0c3cb1951982) |
| Pokémon Ruby / Sapphire | [pret/pokeruby](https://github.com/pret/pokeruby) | [plemulabs/pokeruby](https://github.com/plemulabs/pokeruby) | [5784633c](https://github.com/pret/pokeruby/commit/5784633ce4ef7ade1a7f2d2d0c288e3d5e6cdd7f) |
| Pokémon Mystery Dungeon: Red Rescue Team | [pret/pmd-red](https://github.com/pret/pmd-red) | [plemulabs/pmd-red](https://github.com/plemulabs/pmd-red) | [ce5a84a0](https://github.com/pret/pmd-red/commit/ce5a84a02e9bc5101977908da470fa85fc59e5ff) |
| The Legend of Zelda: The Minish Cap | [zeldaret/tmc](https://github.com/zeldaret/tmc) | [plemulabs/tmc](https://github.com/plemulabs/tmc) | [6fb6dfb4](https://github.com/zeldaret/tmc/commit/6fb6dfb4a7efbe24d0fd1dda5097af6131faacde) |
| Metroid: Zero Mission | [metroidret/mzm](https://github.com/metroidret/mzm) | [plemulabs/mzm](https://github.com/plemulabs/mzm) | [7708d105](https://github.com/metroidret/mzm/commit/7708d105cb3537f941449a9ac74795bb435493fa) |
| Metroid Fusion | [metroidret/mf](https://github.com/metroidret/mf) | [plemulabs/mf](https://github.com/plemulabs/mf) | [de76565c](https://github.com/metroidret/mf/commit/de76565c897c05838503717db9aa2adfe92aeba3) |
| Wario Land 4 | [lilDavid/warioland4](https://github.com/lilDavid/warioland4) | [plemulabs/warioland4](https://github.com/plemulabs/warioland4) | [abb7800a](https://github.com/lilDavid/warioland4/commit/abb7800a8d8fa6d7f7f003627893e06bc2879329) |
| Mario Kart: Super Circuit | [jellees/mksc](https://github.com/jellees/mksc) | [plemulabs/mksc](https://github.com/plemulabs/mksc) | [3df89321](https://github.com/jellees/mksc/commit/3df8932105c91f8e9e1ad72801ea13ff74339fe1) |
| Mario & Luigi: Superstar Saga | [jellees/mlss](https://github.com/jellees/mlss) | [plemulabs/mlss](https://github.com/plemulabs/mlss) | [8db5ad56](https://github.com/jellees/mlss/commit/8db5ad5683841cd536f47020aff626ceec826df8) |
| Sonic Advance 1 / 2 | [SAT-R/sa2](https://github.com/SAT-R/sa2) | [plemulabs/sa2](https://github.com/plemulabs/sa2) | [393357f7](https://github.com/SAT-R/sa2/commit/393357f7c9d46b5c10b6c41a57b80fe3b58f3c8d) |
| Sonic Advance 3 | [SAT-R/sa3](https://github.com/SAT-R/sa3) | [plemulabs/sa3](https://github.com/plemulabs/sa3) | [8f9b9235](https://github.com/SAT-R/sa3/commit/8f9b9235efac449fb2d760a031c35020bab7e414) |
| Fire Emblem: The Binding Blade | [FireEmblemUniverse/fireemblem6j](https://github.com/FireEmblemUniverse/fireemblem6j) | [plemulabs/fireemblem6j](https://github.com/plemulabs/fireemblem6j) | [c5a7f39d](https://github.com/FireEmblemUniverse/fireemblem6j/commit/c5a7f39d6ac3a9c45142f1ccc8f898e62ecceb94) |
| Fire Emblem: The Binding Blade — earlier reference | [StanHash/fe6](https://github.com/StanHash/fe6) | [plemulabs/fe6](https://github.com/plemulabs/fe6) | [f9ea5f67](https://github.com/StanHash/fe6/commit/f9ea5f67f3f1048ca9836d7350077231ba54b589) |
| Fire Emblem: The Sacred Stones | [FireEmblemUniverse/fireemblem8u](https://github.com/FireEmblemUniverse/fireemblem8u) | [plemulabs/fireemblem8u](https://github.com/plemulabs/fireemblem8u) | [04d1edb1](https://github.com/FireEmblemUniverse/fireemblem8u/commit/04d1edb163d14bd10777a065697e1a9f17be65f2) |
| Mega Man Zero 3 / Rockman Zero 3 | [mmzret/rmz3](https://github.com/mmzret/rmz3) | [plemulabs/rmz3](https://github.com/plemulabs/rmz3) | [2a28700e](https://github.com/mmzret/rmz3/commit/2a28700e0a74edd9578737c3b3435ced9d074045) |
| Pokémon Pinball: Ruby & Sapphire | [pret/pokepinballrs](https://github.com/pret/pokepinballrs) | [plemulabs/pokepinballrs](https://github.com/plemulabs/pokepinballrs) | [33ad42e8](https://github.com/pret/pokepinballrs/commit/33ad42e8f2afca891831f03179820b96a3fdef6a) |
| Kirby & The Amazing Mirror | [jiangzhengwenjz/katam](https://github.com/jiangzhengwenjz/katam) | [plemulabs/katam](https://github.com/plemulabs/katam) | [8689e4cc](https://github.com/jiangzhengwenjz/katam/commit/8689e4cc2ea9e03183442a2959f4662789bec3ad) |
| Super Mario World: Super Mario Advance 2 | [KarisaAdvynia/sma2-disasm](https://github.com/KarisaAdvynia/sma2-disasm) | [plemulabs/sma2-disasm](https://github.com/plemulabs/sma2-disasm) | [b75c69fd](https://github.com/KarisaAdvynia/sma2-disasm/commit/b75c69fdb5eb253b85566fbbccf47b5f3d2633e8) |
| Yoshi's Island: Super Mario Advance 3 | [KarisaAdvynia/sma3-disasm](https://github.com/KarisaAdvynia/sma3-disasm) | [plemulabs/sma3-disasm](https://github.com/plemulabs/sma3-disasm) | [c8532ec9](https://github.com/KarisaAdvynia/sma3-disasm/commit/c8532ec9a8d0038c3bfeb003dd0c7ea89d7e1071) |
| Super Mario Advance 4: Super Mario Bros. 3 | [KarisaAdvynia/sma4-disasm](https://github.com/KarisaAdvynia/sma4-disasm) | [plemulabs/sma4-disasm](https://github.com/plemulabs/sma4-disasm) | [f49422e0](https://github.com/KarisaAdvynia/sma4-disasm/commit/f49422e0416f154abe89432d11202641cebc3e3a) |
| Mario vs. Donkey Kong | [camthesaxman/mariovsdk](https://github.com/camthesaxman/mariovsdk) | [plemulabs/mariovsdk](https://github.com/plemulabs/mariovsdk) | [ee1720be](https://github.com/camthesaxman/mariovsdk/commit/ee1720bea222ee4b8762817cd4ef2de64081a74d) |
| Golden Sun | [gsret/goldensun](https://github.com/gsret/goldensun) | [plemulabs/goldensun](https://github.com/plemulabs/goldensun) | [0fa7b312](https://github.com/gsret/goldensun/commit/0fa7b312199c10b96544e825be86cfc476493eb7) |

### SNES (14)

| Game | Original source | PlemuLabs fork | Pinned commit |
| --- | --- | --- | --- |
| Super Mario World | [IsoFrieze/SMWDisX](https://github.com/IsoFrieze/SMWDisX) | [plemulabs/SMWDisX](https://github.com/plemulabs/SMWDisX) | [30643c75](https://github.com/IsoFrieze/SMWDisX/commit/30643c7595a7d097d731de69476f8059c7cf98c3) |
| Super Mario World 2: Yoshi's Island | [brunovalads/yoshisisland-disassembly](https://github.com/brunovalads/yoshisisland-disassembly) | [plemulabs/yoshisisland-disassembly](https://github.com/plemulabs/yoshisisland-disassembly) | [fb79f799](https://github.com/brunovalads/yoshisisland-disassembly/commit/fb79f7994fb19146de35c02fb98fee8af5877372) |
| Super Metroid | [InsaneFirebat/sm_disassembly](https://github.com/InsaneFirebat/sm_disassembly) | [plemulabs/sm_disassembly](https://github.com/plemulabs/sm_disassembly) | [7af131eb](https://github.com/InsaneFirebat/sm_disassembly/commit/7af131ebc328359e852e923603163a329c7aa7af) |
| EarthBound / Mother 2 | [Herringway/ebsrc](https://github.com/Herringway/ebsrc) | [plemulabs/ebsrc](https://github.com/plemulabs/ebsrc) | [bfc7520c](https://github.com/Herringway/ebsrc/commit/bfc7520c9f22b4b67f529b34a0b871c7f5e03705) |
| Final Fantasy IV / Final Fantasy II US | [everything8215/ff4](https://github.com/everything8215/ff4) | [plemulabs/ff4](https://github.com/plemulabs/ff4) | [a360e2ea](https://github.com/everything8215/ff4/commit/a360e2ea7ddc0dc5223bea1db74ebd1a9967280b) |
| Final Fantasy V | [everything8215/ff5](https://github.com/everything8215/ff5) | [plemulabs/ff5](https://github.com/plemulabs/ff5) | [997c87d1](https://github.com/everything8215/ff5/commit/997c87d1d8fdff2c142d91050fe400b6cb293905) |
| Final Fantasy VI / Final Fantasy III US | [everything8215/ff6](https://github.com/everything8215/ff6) | [plemulabs/ff6](https://github.com/plemulabs/ff6) | [81301327](https://github.com/everything8215/ff6/commit/813013276c952fdd27edcf7b8b86f17291542cbf) |
| Donkey Kong Country | [Yoshifanatic1/Donkey-Kong-Country-1-Disassembly](https://github.com/Yoshifanatic1/Donkey-Kong-Country-1-Disassembly) | [plemulabs/Donkey-Kong-Country-1-Disassembly](https://github.com/plemulabs/Donkey-Kong-Country-1-Disassembly) | [c2080f40](https://github.com/Yoshifanatic1/Donkey-Kong-Country-1-Disassembly/commit/c2080f40469c716923f550706509a0d354229841) |
| Donkey Kong Country 2: Diddy's Kong Quest | [p4plus2/DKC2-disassembly](https://github.com/p4plus2/DKC2-disassembly) | [plemulabs/DKC2-disassembly](https://github.com/plemulabs/DKC2-disassembly) | [fb3eff94](https://github.com/p4plus2/DKC2-disassembly/commit/fb3eff9435683652eac354fc61c5a4a66f2faef6) |
| Donkey Kong Country 3: Dixie Kong's Double Trouble! | [Yoshifanatic1/Donkey-Kong-Country-3-Disassembly](https://github.com/Yoshifanatic1/Donkey-Kong-Country-3-Disassembly) | [plemulabs/Donkey-Kong-Country-3-Disassembly](https://github.com/plemulabs/Donkey-Kong-Country-3-Disassembly) | [a7a11515](https://github.com/Yoshifanatic1/Donkey-Kong-Country-3-Disassembly/commit/a7a115152746284f4671b406957b3b1f8dd5993b) |
| Goof Troop | [Yoshifanatic1/Goof-Troop-Disassembly](https://github.com/Yoshifanatic1/Goof-Troop-Disassembly) | [plemulabs/Goof-Troop-Disassembly](https://github.com/plemulabs/Goof-Troop-Disassembly) | [573805ad](https://github.com/Yoshifanatic1/Goof-Troop-Disassembly/commit/573805ade9478ad63ad8d6f411119aeb2bd02685) |
| Super Punch-Out!! | [Yoshifanatic1/Super-Punch-Out-Disassembly](https://github.com/Yoshifanatic1/Super-Punch-Out-Disassembly) | [plemulabs/Super-Punch-Out-Disassembly](https://github.com/plemulabs/Super-Punch-Out-Disassembly) | [3a1bd913](https://github.com/Yoshifanatic1/Super-Punch-Out-Disassembly/commit/3a1bd913e5ff6aefe7c7bcdb2c797919bcea7cba) |
| Super Mario RPG: Legend of the Seven Stars | [Yoshifanatic1/Super-Mario-RPG-Disassembly](https://github.com/Yoshifanatic1/Super-Mario-RPG-Disassembly) | [plemulabs/Super-Mario-RPG-Disassembly](https://github.com/plemulabs/Super-Mario-RPG-Disassembly) | [57cb7076](https://github.com/Yoshifanatic1/Super-Mario-RPG-Disassembly/commit/57cb707669d71bb55817a0f88d28b3018c8bec57) |
| Fire Emblem: Thracia 776 | [ZaneAvernathy/FireEmblem5](https://github.com/ZaneAvernathy/FireEmblem5) | [plemulabs/FireEmblem5](https://github.com/plemulabs/FireEmblem5) | [980bb114](https://github.com/ZaneAvernathy/FireEmblem5/commit/980bb114886061532267a6aa50e4ebd5a37d6d8b) |

### SNES native reconstructions (3)

| Game | Original source | PlemuLabs fork | Pinned commit |
| --- | --- | --- | --- |
| Super Mario World | [snesrev/smw](https://github.com/snesrev/smw) | [plemulabs/smw](https://github.com/plemulabs/smw) | [eae20c65](https://github.com/snesrev/smw/commit/eae20c65c58930c8b62c76188d259579ad4130f1) |
| The Legend of Zelda: A Link to the Past | [snesrev/zelda3](https://github.com/snesrev/zelda3) | [plemulabs/zelda3](https://github.com/plemulabs/zelda3) | [45a149d8](https://github.com/snesrev/zelda3/commit/45a149d8b4bb8098f53d1009f76e76e7d8b79bbf) |
| Super Metroid | [snesrev/sm](https://github.com/snesrev/sm) | [plemulabs/sm](https://github.com/plemulabs/sm) | [578f90b3](https://github.com/snesrev/sm/commit/578f90b3cc49557bb70060ad033bb90b8cf8ac50) |

### N64 (6)

| Game | Original source | PlemuLabs fork | Pinned commit |
| --- | --- | --- | --- |
| Super Mario 64 | [n64decomp/sm64](https://github.com/n64decomp/sm64) | [plemulabs/sm64](https://github.com/plemulabs/sm64) | [9921382a](https://github.com/n64decomp/sm64/commit/9921382a68bb0c865e5e45eb594d9c64db59b1af) |
| Mario Kart 64 | [n64decomp/mk64](https://github.com/n64decomp/mk64) | [plemulabs/mk64](https://github.com/plemulabs/mk64) | [58cfcb02](https://github.com/n64decomp/mk64/commit/58cfcb022e10f83bc3b889d7e97508cae6837098) |
| Banjo-Kazooie | [n64decomp/banjo-kazooie](https://github.com/n64decomp/banjo-kazooie) | [plemulabs/banjo-kazooie](https://github.com/plemulabs/banjo-kazooie) | [e8d31fa5](https://github.com/n64decomp/banjo-kazooie/commit/e8d31fa53645616fcac6e051543222b973a2edb0) |
| The Legend of Zelda: Ocarina of Time | [zeldaret/oot](https://github.com/zeldaret/oot) | [plemulabs/oot](https://github.com/plemulabs/oot) | [14759abf](https://github.com/zeldaret/oot/commit/14759abf9abb4295de142cdc1452998630ea70fb) |
| The Legend of Zelda: Majora's Mask | [zeldaret/mm](https://github.com/zeldaret/mm) | [plemulabs/mm](https://github.com/plemulabs/mm) | [710e1a7d](https://github.com/zeldaret/mm/commit/710e1a7d50a1f987f5fc55abca37f7fdcc8ee43d) |
| Paper Mario | [pmret/papermario](https://github.com/pmret/papermario) | [plemulabs/papermario](https://github.com/plemulabs/papermario) | [222af07f](https://github.com/pmret/papermario/commit/222af07f2ce4250c1eb70f751fefe8a8476fae96) |

## Verification and updates

[Live fork verification](verification.json) confirms all 51 direct fork parents and pinned commits are available through their organization forks. [catalog.json](catalog.json) records upstream/fork repository IDs, direct fork parents, verification dates and commit pins. [The verifier](scripts/verify-catalog.py) checks all 51 original URLs, distinct forks, staged/committed gitlinks, clean initialized checkouts and exact roster coverage. Use `--metadata-only` before initializing submodules.

Updating a submodule is an explicit Git change: inspect upstream changes, select a commit, update its matching manifest entry, run the verifier and commit the new pin. Fork default branches and original repositories can move independently; this catalog remains pinned until updated.
