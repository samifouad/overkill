"""Verify a built dedicated server loads Excessive without setting fs_game.

Usage: python3 tests/excessive-smoke.py build/Release/ioq3ded-excessive
Uses a generated empty BSP, so no proprietary Quake 3 data is needed.
"""

import pathlib
import re
import shutil
import struct
import subprocess
import sys
import tempfile


def empty_map():
    lumps = [b""] * 17
    lumps[0] = b'{\n"classname" "worldspawn"\n}\n' + b'\0'
    lumps[1] = struct.pack("<64sii", b"smoke", 0, 0)
    lumps[2] = struct.pack("<4f", 1, 0, 0, 0)
    lumps[3] = struct.pack("<9i", 0, -1, -1, -1024, -1024, -1024, 1024, 1024, 1024)
    lumps[4] = struct.pack("<12i", -1, 0, -1024, -1024, -1024, 1024, 1024, 1024, 0, 0, 0, 0)
    lumps[7] = struct.pack("<6f4i", -1024, -1024, -1024, 1024, 1024, 1024, 0, 0, 0, 0)
    header = b"IBSP" + struct.pack("<i", 46)
    data = b""
    for lump in lumps:
        header += struct.pack("<ii", 144 + len(data), len(lump))
        data += lump
        data += b"\0" * (-len(data) % 4)
    return header + data


server = pathlib.Path(sys.argv[1]).resolve()
mod = server.parent / "excessive"
if not (mod / "vm/qagame.qvm").is_file():
    sys.exit(f"Missing deployed Excessive VM beside {server}")

with tempfile.TemporaryDirectory(prefix="overkill-smoke-") as temporary:
    root = pathlib.Path(temporary)
    shutil.copytree(mod, root / "excessive")
    game = root / "smoketest"
    (game / "maps").mkdir(parents=True)
    (game / "default.cfg").write_text("set bot_enable 0\n")
    (game / "maps/smoke.bsp").write_bytes(empty_map())

    arguments = [str(server), "+set", "com_basegame", "smoketest",
                 "+set", "fs_basepath", str(root),
                 "+set", "fs_homepath", str(root / "home"),
                 "+set", "net_enabled", "0"]
    result = subprocess.run(arguments + ["+map", "smoke", "+fs_game",
                            "+ex_instant", "+ex_quadstart", "+quit"],
                            cwd=root, capture_output=True, text=True, timeout=30)
    output = result.stdout + result.stderr
    expected = [r'"fs_game" is:"excessive', r'gamename: Excessive',
                r'File "vm/qagame.qvm" found at ".*[/\\]excessive"',
                r'"ex_instant" is:"1', r'"ex_quadstart" is:"1']
    if result.returncode or any(not re.search(pattern, output) for pattern in expected):
        sys.exit(output)

    # Explicitly selecting the base game must still override the default.
    result = subprocess.run(arguments + ["+set", "fs_game", "", "+fs_game", "+quit"],
                            cwd=root, capture_output=True, text=True, timeout=30)
    output = result.stdout + result.stderr
    if result.returncode or not re.search(r'"fs_game" is:"\^7"', output):
        sys.exit(output)

print("PASS: default startup loads the Excessive VM and enables its gameplay; explicit base-game override works.")
