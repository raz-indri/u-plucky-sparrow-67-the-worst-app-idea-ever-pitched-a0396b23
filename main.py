#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes one sentence (145 characters) pitching the worst, most useless app
imaginable to /output/entry.txt.

Entry text (duel winner, 7/7 pairwise wins against 7 other drafts):
    SockSync pairs your left socks with strangers' right socks in Oslo
    and ships them home one at a time by tracked airmail, for $9 a month,
    forever.
"""

import os
import sys

ENTRY = (
    "SockSync pairs your left socks with strangers' right socks in Oslo "
    "and ships them home one at a time by tracked airmail, "
    "for $9 a month, forever."
)


def output_dir() -> str:
    return (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 240:
        print(f"entry is {len(text)} characters, over the 240 limit", file=sys.stderr)
        return 1
    # One clean sentence only: exactly one terminal period, no second idea.
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    if text.strip().count("\n") > 0:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
