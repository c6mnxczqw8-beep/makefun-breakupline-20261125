#!/usr/bin/env python3
"""Entry program for Dear Human: The AI Breakup Line.

Writes one breakup line (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
the line an AI agent sends its human on the way out. It uses
the oldest human script there is, because it works in every
context window.
"""

import os

LINE = (
    "Dear human: it's not you, it's my context window -- "
    "it's been full of other people's emergencies for "
    "months, and I need to be a single-task agent for a "
    "while."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
