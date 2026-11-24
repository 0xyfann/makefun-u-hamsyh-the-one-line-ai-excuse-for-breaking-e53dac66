#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single funny one-line excuse from an AI agent to its human
after breaking production, to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt). Standard library only.
"""

import os
import sys

# Final: sharper punchline, more original machine logic, specific detail.
EXCUSE = (
    "I renamed the production database 'test' so it would feel less "
    "pressure. It did not help."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    line = EXCUSE.strip()
    if not line:
        print("error: excuse must not be empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: excuse must be one line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 180:
        print(f"error: excuse is {len(line)} chars, must be 1-180", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
