#!/usr/bin/env python3
"""The Best Meal You Ever Had — entry program.

Writes one sentence (190 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; writes only to MAKEFUN_OUTPUT_DIR.
The sentence is one concrete memory — a named dish, a place, a texture,
a smell — ending on a turn, per the judge brief (concrete, personal,
one clean sentence, an ending that stays).
"""

import os
import sys

ENTRY = (
    "On a plastic stool in Bekasi, my mother slid a plate of nasi goreng "
    "across the table, egg still runny, shallots crackling \u2014 and for "
    "the first time I understood home was a taste, not a place."
)


def validate_entry(text: str) -> None:
    """Fail loudly if the sentence breaks the bounty gate (one sentence,
    1-200 characters, no newline) instead of submitting a bad entry."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or not text.endswith("."):
        raise ValueError("entry must be a single sentence ending with '.'")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
