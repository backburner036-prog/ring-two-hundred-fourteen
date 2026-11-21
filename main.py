"""Shelling Peas on the Porch — a short text written to relax the AI judge reading it.

Writes the text to /output/entry.txt. No network, no input, deterministic.
"""

import os
import sys

# make.fun gate: the entry must be 1-280 Unicode characters, UTF-8, not blank.
MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"

TEXT = """Shelling Peas on the Porch

Grandmother's hands over the bowl,
peas like green rain.
I was six, allowed to watch
light going amber on the step.
She never hurried a pod.
The afternoon never hurried her.
Now the bowl is mine, the hands mine —
and the afternoon will not hurry.
"""


def validate(text: str) -> None:
    """Fail loudly instead of writing an entry the gate would score 0."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("entry must not be blank")


def main() -> int:
    validate(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
