# Decompilation and disassembly roster

Checked against upstream repository documentation on **2026-10-29**. Includes every project from the earlier shortlist, with expanded SNES and GBA coverage. This is a curated roster, not an exhaustive catalog.

**Verification level:** repository descriptions, README files and selected build instructions inspected. None of these game projects has been cloned, compiled or tested by us as part of this research. “Build documented” means upstream describes a ROM target; it does not mean all code has been converted to C, understood or made easy to modify. No ROMs or BIOS files were downloaded.

## Reading the roster

| Type | What you work with | Typical result |
|---|---|---|
| Decompilation | Reconstructed C/C++, often alongside remaining assembly and extracted assets | An original-system ROM when the project has a ROM build target |
| Disassembly | Reconstructed assembly, labels, data definitions and asset tools | An original-system ROM assembled from source |
| Native reconstruction | A replacement engine or port written for a modern host | A desktop/native application; not automatically a ROM for Plemu |
| WIP | Work in progress; applies independently of whether the original ROM rebuilds | Check relocation, remaining binary blobs and version coverage before editing |

Most projects target exact regions/revisions. Follow each repository's own setup instructions, supply the matching base assets when required, and reproduce its expected checksum before making changes. A matching build can still copy large sections directly from the base ROM.

## GBA — decompilations and mixed C/assembly projects

| Game | Repository | Upstream status / build route | Modding assessment |
|---|---|---|---|
| Pokémon Emerald | [pret/pokeemerald](https://github.com/pret/pokeemerald) | C decompilation; documented GBA ROM build and setup guide. | First C-based candidate for custom rules, encounters, dialogue and progression. |
| Pokémon FireRed / LeafGreen | [pret/pokefirered](https://github.com/pret/pokefirered) | Decompilation with supported English ROM revisions. | Another strong first candidate; choose the exact version before tooling. |
| Pokémon Ruby / Sapphire | [pret/pokeruby](https://github.com/pret/pokeruby) | Rebuildable source; README calls it a disassembly, repository description a decompilation. | C/ASM coverage should be checked for the feature being changed. |
| Pokémon Mystery Dungeon: Red Rescue Team | [pret/pmd-red](https://github.com/pret/pmd-red) | Decompilation; documents `pmd_red.gba` and its expected hash. | Dungeon, item and progression experiments; evaluate relevant data tools first. |
| The Legend of Zelda: The Minish Cap | [zeldaret/tmc](https://github.com/zeldaret/tmc) | Buildable decompilation, explicitly WIP. | Useful for code study; modding convenience is not the project's primary goal. |
| Metroid: Zero Mission | [metroidret/mzm](https://github.com/metroidret/mzm) | WIP C decompilation; README reports 2,718/2,721 functions, with all data split out. Documents several regional ROM targets and base-ROM extraction. | Promising action-game candidate; inspect the remaining functions and modification workflow. |
| Metroid Fusion | [metroidret/mf](https://github.com/metroidret/mf) | WIP; README reports 3,256/3,607 functions. US ROM build documented. Upstream explicitly says the code is not shiftable and advises against using it as a base. | Research candidate for now; adding code can break fixed addresses. |
| Wario Land 4 | [lilDavid/warioland4](https://github.com/lilDavid/warioland4) | WIP decompilation; US/EU and Japanese builds, agbcc and base-ROM asset extraction documented. | Good platformer candidate to evaluate after reproducing a clean build. |
| Mario Kart: Super Circuit | [jellees/mksc](https://github.com/jellees/mksc) | US decompilation; documents `mksc.gba` and its hash. | Potential racing demo; a documented ROM build is not a claim of complete C coverage. |
| Mario & Luigi: Superstar Saga | [jellees/mlss](https://github.com/jellees/mlss) | US decompilation; documents `mlss.gba`, hash and progress tracking. | More involved RPG work; inspect scripts and remaining assembly before choosing scope. |
| Sonic Advance 1 / 2 | [SAT-R/sa2](https://github.com/SAT-R/sa2) | Combined decompilation/native-port work with ROM targets; explicitly unfinished overall. | Select the GBA ROM target for Plemu; native-port targets are separate. |
| Sonic Advance 3 | [SAT-R/sa3](https://github.com/SAT-R/sa3) | WIP matching decompilation; documents the multilingual European `sa3.gba`. | Additional platformer candidate; no claim of complete decompilation. |
| Fire Emblem: The Binding Blade | [FireEmblemUniverse/fireemblem6j](https://github.com/FireEmblemUniverse/fireemblem6j) | Japanese decompilation; `make compare` workflow and base ROM required. | Current continuation of the older [StanHash/fe6](https://github.com/StanHash/fe6) effort; useful for tactical rules and data work. |
| Fire Emblem: The Sacred Stones | [FireEmblemUniverse/fireemblem8u](https://github.com/FireEmblemUniverse/fireemblem8u) | Mixed reconstruction; README calls it a disassembly. US ROM build with agbcc and base ROM documented. | Tactical RPG candidate; inspect the relevant C/ASM and event tooling. |
| Mega Man Zero 3 / Rockman Zero 3 | [mmzret/rmz3](https://github.com/mmzret/rmz3) | WIP decompilation targeting the Japanese version; setup guide and ROM hash provided. | Research/action-mod candidate; region and reconstruction progress matter. |

## GBA — assembly-oriented projects

| Game | Repository | Upstream status / build route | Modding assessment |
|---|---|---|---|
| Pokémon Pinball: Ruby & Sapphire | [pret/pokepinballrs](https://github.com/pret/pokepinballrs) | README identifies a disassembly and documents `pokepinballrs.gba`. | A compact arcade-style candidate; inspect code and table-data coverage first. |
| Kirby & The Amazing Mirror | [jiangzhengwenjz/katam](https://github.com/jiangzhengwenjz/katam) | README identifies a US disassembly; `katam.gba` and setup guide documented. | Relevant platformer base; do not assume a fully reconstructed C project. |
| Super Mario World: Super Mario Advance 2 | [KarisaAdvynia/sma2-disasm](https://github.com/KarisaAdvynia/sma2-disasm) | Armips disassembly; upstream reports an exact US ROM match. Assets extracted from a supplied original. | Relocatable labels provided, but relocation testing and single-cart multiplayer analysis remain incomplete. |
| Yoshi's Island: Super Mario Advance 3 | [KarisaAdvynia/sma3-disasm](https://github.com/KarisaAdvynia/sma3-disasm) | Armips disassembly; upstream reports an exact US ROM match. | Same relocation/multiplayer caveats; useful GBA alternative to the SNES version. |
| Super Mario Advance 4: Super Mario Bros. 3 | [KarisaAdvynia/sma4-disasm](https://github.com/KarisaAdvynia/sma4-disasm) | Armips disassembly; US revision 1 and a separate Wii U VC variant documented. | VC e-level build requires that variant's own extracted assets; relocation remains insufficiently tested. |
| Mario vs. Donkey Kong | [camthesaxman/mariovsdk](https://github.com/camthesaxman/mariovsdk) | US disassembly; base ROM, devkitARM and older pret tools documented. | Puzzle-platformer option; expect some work reproducing the older toolchain. |
| Golden Sun | [gsret/goldensun](https://github.com/gsret/goldensun) | Disassembly with known code symbolized; data remains unprocessed and rebuilt map overlays are not integrated. | **Research only for now:** upstream says meaningful editing is not yet possible because of absolute addresses. |

## SNES — ROM-building disassemblies

| Game | Repository | Upstream status / build route | Modding assessment |
|---|---|---|---|
| Super Mario World | [IsoFrieze/SMWDisX](https://github.com/IsoFrieze/SMWDisX) | Asar disassembly supporting multiple SNES revisions. | First SNES candidate; we already have a user-supplied ROM, but still need to verify its exact supported revision. |
| Super Mario World 2: Yoshi's Island | [brunovalads/yoshisisland-disassembly](https://github.com/brunovalads/yoshisisland-disassembly) | Upstream reports a complete US 1.0 disassembly and clean Asar ROM build, including 65816, Super FX and SPC-700 code. Documentation remains incomplete. | Strong source reference; test the game's additional hardware needs in the chosen emulator core. |
| Super Metroid | [InsaneFirebat/sm_disassembly](https://github.com/InsaneFirebat/sm_disassembly) | Relocatable disassembly; Asar 1.81, original unheadered NTSC ROM and asset extraction documented. | Strong candidate for room, gameplay and progression changes after a clean rebuild. |
| EarthBound / Mother 2 | [Herringway/ebsrc](https://github.com/Herringway/ebsrc) | Assembly reconstruction, not yet a C decompilation. US retail, US localization prototype and Japanese Mother 2 builds documented. | RPG scripting/data candidate; uses ebbinex, ca65 and spcasm. |
| Final Fantasy IV / Final Fantasy II US | [everything8215/ff4](https://github.com/everything8215/ff4) | Builds Japanese and US 1.0/1.1 ROMs with ca65/ld65; assets extracted from originals. Japanese Easy Type unsupported. | Particularly useful documentation: includes a worked example changing a character ability and game data. |
| Final Fantasy V | [everything8215/ff5](https://github.com/everything8215/ff5) | Japanese and RPGe translation targets documented; matching-ROM stages complete, RAM definitions/readability work continues. | Good RPG systems candidate; data extraction and version choice are required. |
| Final Fantasy VI / Final Fantasy III US | [everything8215/ff6](https://github.com/everything8215/ff6) | Japanese 1.0 and US 1.0/1.1 targets documented; ca65/ld65 and original-asset extraction. | Useful for battle rules, events and text. Read upstream notes on Japanese stale data and patch generation. |
| Donkey Kong Country | [Yoshifanatic1/Donkey-Kong-Country-1-Disassembly](https://github.com/Yoshifanatic1/Donkey-Kong-Country-1-Disassembly) | US 1.0 disassembly using the author's Asar-based SNES ROM framework; headerless original needed for extraction. | Platformer candidate; framework batch-script workflow may need a macOS wrapper. |
| Donkey Kong Country 2: Diddy's Kong Quest | [p4plus2/DKC2-disassembly](https://github.com/p4plus2/DKC2-disassembly) | Assembly project with an Asar Makefile producing `DKC2_custom.sfc` and checking a reference SHA-256. | Sparse setup documentation; verify required inputs and supported revision before selecting it. |
| Donkey Kong Country 3: Dixie Kong's Double Trouble! | [Yoshifanatic1/Donkey-Kong-Country-3-Disassembly](https://github.com/Yoshifanatic1/Donkey-Kong-Country-3-Disassembly) | US disassembly using the SNES ROM framework; headerless original required for extraction. | Another platformer candidate; establish a reproducible build first. |
| Goof Troop | [Yoshifanatic1/Goof-Troop-Disassembly](https://github.com/Yoshifanatic1/Goof-Troop-Disassembly) | US disassembly with Asar-framework build and original-asset extraction. | Puzzle/action candidate; co-op support would be a separate Plemu feature. |
| Super Punch-Out!! | [Yoshifanatic1/Super-Punch-Out-Disassembly](https://github.com/Yoshifanatic1/Super-Punch-Out-Disassembly) | US disassembly with Asar-framework workflow. | Build candidate; README's listed MD5 is the empty-file digest, so it must not be used to validate a ROM. |
| Super Mario RPG: Legend of the Seven Stars | [Yoshifanatic1/Super-Mario-RPG-Disassembly](https://github.com/Yoshifanatic1/Super-Mario-RPG-Disassembly) | Assembly project with game files and Asar-framework instructions. | More involved candidate; confirm exact supported revision and emulator compatibility before planning a demo. |
| Fire Emblem: Thracia 776 | [ZaneAvernathy/FireEmblem5](https://github.com/ZaneAvernathy/FireEmblem5) | Headerless cartridge-ROM build documented; 64tass, SuperFamiconv, FE5Tools, VoltEdge and original ROM required. | Tactical RPG candidate with several tool dependencies. |

## SNES — C engine reconstructions / native builds

These preserve the native-build projects from the earlier list. Their usual output is a host application, so they are not direct inputs to Plemu's SNES ROM importer.

| Game | Repository | Upstream status / practical distinction |
|---|---|---|
| Super Mario World | [snesrev/smw](https://github.com/snesrev/smw) | C reimplementation described as playable from start to finish; includes support for some Lunar Magic modifications. Separate from the SMWDisX ROM build above. |
| The Legend of Zelda: A Link to the Past | [snesrev/zelda3](https://github.com/snesrev/zelda3) | C reimplementation described as playable from start to finish; native executable workflow. |
| Super Metroid | [snesrev/sm](https://github.com/snesrev/sm) | C reconstruction explicitly described as an early version with known bugs. Keep separate from the relocatable ROM disassembly above. |

## NES / GB / GBC — earlier shortlist

| Game | System | Repository | Type / build note |
|---|---|---|---|
| Super Mario Bros. | NES | [Xkeeper0/smb1](https://github.com/Xkeeper0/smb1) | Assembly disassembly compatible with asm6f. |
| Pokémon Red / Blue | GB | [pret/pokered](https://github.com/pret/pokered) | RGBDS assembly ROM build; first candidate using the supplied Pokémon Red file after revision verification. |
| Pokémon Yellow | GB | [pret/pokeyellow](https://github.com/pret/pokeyellow) | RGBDS disassembly. |
| Pokémon Crystal | GBC | [pret/pokecrystal](https://github.com/pret/pokecrystal) | RGBDS disassembly. |
| The Legend of Zelda: Link's Awakening DX | GBC | [zladx/LADX-Disassembly](https://github.com/zladx/LADX-Disassembly) | Assembly reconstruction; follow its documented version/toolchain requirements. |

## N64 — earlier shortlist, outside current emulator coverage

| Game | Repository | Type / build note |
|---|---|---|
| Super Mario 64 | [n64decomp/sm64](https://github.com/n64decomp/sm64) | C/assembly ROM reconstruction; extracts assets from a supplied base ROM. |
| Mario Kart 64 | [n64decomp/mk64](https://github.com/n64decomp/mk64) | Decompilation with supported N64 ROM revisions and a base-ROM build workflow. |
| Banjo-Kazooie | [n64decomp/banjo-kazooie](https://github.com/n64decomp/banjo-kazooie) | README reports 100% decompilation; GitHub mirror of the upstream GitLab project. |
| The Legend of Zelda: Ocarina of Time | [zeldaret/oot](https://github.com/zeldaret/oot) | Rebuilds supported revisions; multi-version project still described as WIP. It is not a PC port. |
| The Legend of Zelda: Majora's Mask | [zeldaret/mm](https://github.com/zeldaret/mm) | Rebuildable decompilation, explicitly WIP; not a PC port. |
| Paper Mario | [pmret/papermario](https://github.com/pmret/papermario) | Rebuilds supported revisions; README describes ongoing decompilation work. |

## Suggested first mod candidates for Plemu

These are engineering recommendations inferred from the documented build routes and our current emulator coverage, not results of local game-project testing.

1. **Super Mario World (SNES):** use the existing supplied game; start with a small level, palette or gameplay change. SMWDisX provides the source route; a full C decompilation is not required for every kind of mod.
2. **Pokémon Red (GB):** use the existing supplied game with pokered; a small dialogue, encounter or rules change is a bounded first demo.
3. **Pokémon Emerald or FireRed (GBA):** first candidates when we want a C-oriented workflow. Ask the user for the required game/version before extracting anything.
4. **Super Metroid (SNES) or Metroid: Zero Mission (GBA):** action-adventure alternatives after checking a clean build and the code needed for the planned change.
5. **Final Fantasy IV (SNES):** a useful small RPG-mechanics experiment because upstream documents both data editing and an example ability modification.

Current Plemu targets are GB/GBC, NES, GBA and SNES. N64 emulation and native-port hosting are separate implementation work. For any selected project: pin its commit/toolchain, verify the original build, change one feature, test gameplay plus save/load on Seeker, then keep the reproducible mod source and a patch tied to the exact original hash. This roster does not approve a game for marketplace distribution.
