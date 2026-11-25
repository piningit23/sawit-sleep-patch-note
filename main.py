"""Fix Human Sleep: Funniest Patch Note.

Writes a single patch-note line announcing that human sleep is fixed
to /output/entry.txt. Deterministic, Python 3.13 stdlib only.
"""

import os

ENTRY = (
    "Fixed a bug where sleep ended after eight hours regardless of "
    "whether the human was rested; sleep now saves progress instead "
    "of just pausing the game."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
