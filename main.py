"""Quiet Dread — a one-line code review comment.

Writes a single line to the entry file: an approval carrying quiet
existential dread. Standard library only.
"""

import os

COMMENT = "LGTM. This code will outlive us all and never once think of us."


def resolve_output_path():
    """Pick the output file: ENTRY_OUTPUT wins, then an output dir, else default."""
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def validate(text):
    """The gate: one line, 1-140 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("comment must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("comment must be a single line")
    if not text.strip():
        raise ValueError("comment must not be only whitespace")
    if text != text.strip():
        raise ValueError("comment must not start or end with whitespace")
    if not 1 <= len(text) <= 140:
        raise ValueError("comment must be 1-140 characters, got %d" % len(text))


def main():
    validate(COMMENT)
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(COMMENT)


if __name__ == "__main__":
    main()
