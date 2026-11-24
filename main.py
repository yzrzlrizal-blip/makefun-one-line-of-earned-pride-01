#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun bounty u-mang-one-line-of-earned-pride-a0138557.

Writes a single line of text (1-240 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output): a quiet, earned moment of pride for someone in a scene.
Pure standard library; deterministic — the same bytes on every run.
"""

import os
import sys

# The entry: one line, a small person doing something hard, a long effort
# finally landing — the pride earned inside the line, never asserted.
LINE = (
    "After eleven ruined loaves, the apprentice pulled one from the oven "
    "that sang when tapped — and her master, without a word, slid the "
    "shop keys across the counter to her."
)

MAX_CHARS = 240


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read and verify the bytes we wrote.
    with open(path, "rb") as f:
        if f.read() != data:
            print("verification failed: entry.txt differs", file=sys.stderr)
            return 1
    print(f"wrote {len(data)} bytes ({len(line)} chars) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
