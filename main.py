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

# Bounty gate (from the competition kit): UTF-8, 1-200 characters,
# not only whitespace, one sentence.
_MAX_CHARS = 200
_SENTENCE_ENDERS = ".!?"


def validate_entry(text: str) -> None:
    """Fail loudly if the sentence breaks the bounty gate instead of
    submitting a bad entry.

    Checks, in order: length 1-200 characters, not whitespace-only,
    no control characters (which would corrupt the plain-text output),
    a single sentence (exactly one sentence-ending mark, at the end),
    and no embedded newline.
    """
    if not 1 <= len(text) <= _MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    enders = [ch for ch in text if ch in _SENTENCE_ENDERS]
    if len(enders) != 1 or not text.endswith(enders[0]):
        raise ValueError("entry must be exactly one sentence")


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
