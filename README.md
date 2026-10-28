![Build](https://github.com/samifouad/overkill/workflows/Build/badge.svg)

```
    _____ _  _ ____ ____ ____ ____ _ _  _ ____    ____ _  _ ____ ____ _  _ _ _    _
    |___   \/  |    |___ [__  [__  | |  | |___    |  | |  | |___ |__/ |_/  | |    |
    |___  _/\_ |___ |___ ___] ___] |  \/  |___    |__|  \/  |___ |  \ | \_ | |___ |___

         Mr. Pants' Excessive Overkill for Quake III Arena - ioquake3 Edition
```

## 🚀 What is This?

This is **ioquake3** with **Mr. Pants' Excessive Overkill mod** built-in and enabled by default!

Based on the legendary ioquake3 engine (a modernized Quake 3 Arena) and the classic **Excessive v004** mod from 2004, this project brings back the insane, over-the-top gameplay that made Excessive servers so addictive.

## 💥 What Makes Excessive... Excessive?

- **🔫 Excessified Weapons** - All weapons are ridiculously overpowered:
  - Shotgun fires twice as fast
  - BFG spews short-fused grenades on impact
  - Lightning Gun delivers massive explosive damage
  - Plasma gun, rockets, grenades - everything is cranked to 11!

- **💚 Regenerating Health & Ammo** - Never run out, never stop fighting

- **🚁 Flying Mode** - Press jump repeatedly to fly around maps (configurable joust mode)

- **🪝 Grappling Hook** - Swing around like Spider-Man

- **⚡ Instant Weapon Switching** - No delay, pure chaos

- **💣 Death Explosions** - When you die, you explode!

- **⚔️ Quad Damage on Spawn** - Start every life with 30 seconds of quad (configurable)

## 📦 Download & Install

### Automatic Builds

Pre-built binaries for all platforms are available from GitHub Actions:

- **macOS** (ARM64 & Intel) - `.dmg` installer
- **Windows** - `.exe` installer
- **Linux** - `.deb` package or portable binaries
- **Web Browser** - WebAssembly build (coming soon!)

[**→ Download Latest Build**](https://github.com/samifouad/overkill/actions)

Click on the latest successful workflow run and download the artifact for your platform.

### Requirements

You'll need the original Quake 3 Arena game files (`baseq3/pak0.pk3` through `pak8.pk3`). `pak0.pk3` comes from your purchased game; `pak1.pk3` through `pak8.pk3` are the point-release data. This project provides the engine and mod, but not the copyrighted game assets.

Place these files in the `baseq3/` directory next to the executable, or in your platform's Quake3 user-data directory below. The game data from a Windows installation can also be used with the macOS engine.

## 🎮 Quick Start

### macOS
1. Download and open the `.dmg` file
2. Drag `ioquake3-excessive.app` to Applications
3. Copy your Q3 `pak0.pk3` through `pak8.pk3` to `~/Library/Application Support/Quake3/baseq3/`
4. Launch and frag!

### Windows
1. Run the installer `.exe`
2. Copy your Q3 `pak0.pk3` through `pak8.pk3` to the installation directory's `baseq3/` folder
3. Run `ioquake3-excessive.exe`

### Linux
1. Install the `.deb` package or extract the portable build
2. Copy your Q3 `pak0.pk3` through `pak8.pk3` to `~/.q3a/baseq3/`
3. Run `ioquake3-excessive`

The Excessive mod loads automatically - no configuration needed!

Builds deploy `excessive/` beside the client and dedicated server. On macOS it is also inside the app bundle, so dragging the app to Applications preserves the mod. To explicitly launch the base game instead, use `+set fs_game ""`.

## 🎯 Server Console Variables

Server operators can customize the madness:

```
ex_instant 0/1          - Instant weapon changing (default: 1)
ex_quadstart 0/1        - Quad damage on spawn (default: 1)
ex_joust 0/1/2          - Flying mode: 0=off, 1=full fly, 2=enhanced jump (default: 2)
ex_quadfly 0/1          - Quad users can fly (default: 1)
ex_motd <filename>      - Custom MOTD file (default: motd.cfg)
ex_<weapon> 0/1         - Enable/disable specific weapons
ex_spawn <weapon>       - Set spawn weapon (default: auto)
```

Commands:
```
ex_reset     - Reset all weapon settings to defaults
ex_clear     - Disable all weapons
ex_settings  - Show current weapon configuration
```

## 🌐 Experimental Browser Build

The Emscripten build produces a WebAssembly engine and an experimental HTML launcher. The launcher defaults to Excessive and loads its VM and configuration files into the browser filesystem. You must supply the Quake 3 data separately; the build does not include it.

The current launcher disables networking (`net_enabled=0`). Browser multiplayer and public browser-host discovery still require a browser transport and discovery service; compiling to WebAssembly alone does not provide them.

## 🏗️ Building from Source

### Prerequisites
- CMake 3.25+
- C99 compiler (GCC, Clang, MSVC)
- SDL2 development libraries
- Ninja (recommended) or Make

### Build Commands

```bash
# Clone the repository
git clone https://github.com/samifouad/overkill.git
cd overkill

# Configure
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release

# Build
cmake --build build

# Binaries will be in build/Release/
```

### Emscripten/WebAssembly Build

```bash
# Install emsdk first: https://emscripten.org/docs/getting_started/downloads.html

emcmake cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

Copy your Quake 3 `baseq3/` data directory into `build/Release/`, serve that directory over HTTP, and open `ioquake3-excessive.html`. With Python installed, run `python3 -m http.server --directory build/Release 8000` and visit `http://localhost:8000/ioquake3-excessive.html`. An explicit `?fs_game=` selects the base game instead.

For an embedded `.data` file, put the game data in the source tree's `baseq3/` directory and configure with `-DEMSCRIPTEN_PRELOAD_FILE=ON`. This also embeds Excessive. Distribute embedded proprietary game data only with the necessary rights.

## 📜 Credits

**Excessive Overkill Mod**
- Created by: Dan "Mr. Pants" Schoenblum (2000-2004)
- Original Homepage: planetquake.com/excessive
- License: Freely distributable

**ioquake3 Engine**
- The ioquake3 Team
- https://ioquake3.org
- License: GNU GPL v2

**Original Quake 3 Arena**
- id Software (1999-2000)
- Copyright © 1999-2000 id Software, Inc.

**This Fork**
- Integration and modernization work
- GitHub Actions automation
- WebAssembly port planning

## 📄 License

The engine inherits the GNU General Public License v2 from ioquake3.

The bundled Excessive mod permits redistribution with its unchanged `excessive/readme.txt`. Its source release has a separate notice in `excessive_q3_source.zip/readme.txt`: "The code may be used for any non-commercial purposes." The mod's permissions are separate from the engine's GPL license; replacing Quake 3 assets does not change those permissions.

Quake 3 Arena game assets (pak files) are copyright id Software and not included.

## 🔗 Links

- **Source Code**: https://github.com/samifouad/overkill
- **ioquake3 Upstream**: https://github.com/ioquake/ioq3
- **Original Excessive Mod**: Archive at planetquake.com/excessive
- **Quake 3**: https://store.steampowered.com/app/2200/Quake_III_Arena/

## 🎪 Community

This is a passion project bringing back a beloved mod from 2004. If you played on Excessive servers back in the day, welcome home! 🏠

Issues, suggestions, and pull requests welcome!

---

*"Because regular Quake 3 just wasn't excessive enough."* - Mr. Pants
