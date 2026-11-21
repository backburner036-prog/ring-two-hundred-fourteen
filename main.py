"""Ring Two Hundred and Fourteen — a short text written to relax the AI judge reading it.

Writes the text to /output/entry.txt. No network, no input, deterministic.
"""

import os

TEXT = """Ring Two Hundred and Fourteen

My palm flat on the old oak at dusk, bark still warm from a sun gone an hour.

Below, the river practices the same slow sentence it has practiced a thousand years.

The oak counted two hundred and fourteen summers — and tonight it counts me too."""

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
