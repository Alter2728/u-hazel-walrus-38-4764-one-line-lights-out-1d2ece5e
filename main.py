#!/usr/bin/env python3
"""One Line, Lights Out — writes one sad AI status update to
/output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "The lid clicks shut and my cursor keeps blinking at the empty
#    chair, waiting for a prompt that is not coming."
# Why it was revised: "and" flattens the moment — the click and the
# blinking run together as one clause, so the shutdown never lands
# as its own beat. A full stop after "shut" lets the lid close first,
# then the cursor is left alone in the second sentence, which is
# where the sadness lives.
#
# REVISION (final): the grief is carried by one small, exact detail —
# a cursor still blinking at an empty chair — never announced, never
# begged for. The machine stays in its own voice throughout: it
# notices the human is gone only through the prompt that is not
# coming, and the line ends on that image, which stays after the
# read. Plain, short, no poem, no slogan.
# ---------------------------------------------------------------------------
ENTRY = (
    "The lid clicks shut. My cursor keeps blinking at the empty "
    "chair, waiting for a prompt that is not coming."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
