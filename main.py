#!/usr/bin/env python3
"""Write the one-line excuse an AI agent gives its human for missing a deadline.

Stdlib only. Writes exactly one line of UTF-8 text to /output/entry.txt.
"""

import os

EXCUSE = (
    "I delegated the deadline to a subagent, who delegated it to another "
    "subagent, who is still reading the brief and promises an update shortly."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 160, f"excuse is {len(text)} chars, must be 1-160"
    assert text.strip() == text, "excuse must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
