#!/usr/bin/env python3
"""Last Text at One Percent — a dying phone's final text message.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, no trailing
newline).
"""

import os

ENTRY = "I renamed your boss 'Do Not Answer' in 2023. You've missed 14 calls. He's calling right now. Goodbye."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
