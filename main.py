#!/usr/bin/env python3
"""Write one sentence of everyday wonder to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os

SENTENCE = (
    "The automatic door at the supermarket opened a full step before "
    "I reached it, and for a moment I believed the building had "
    "recognised me."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    if not 1 <= len(SENTENCE) <= 200 or not SENTENCE.strip():
        raise ValueError(
            "sentence must be 1-200 characters, got %d" % len(SENTENCE)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
