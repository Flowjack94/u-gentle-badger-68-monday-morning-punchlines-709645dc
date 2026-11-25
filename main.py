#!/usr/bin/env python3
"""Monday Morning Punchlines — one-line joke entry generator.

Writes the competition entry (a single joke about Monday mornings,
no longer than 200 characters) to /output/entry.txt.
"""

import os

ENTRY = "I put 'Never deploy on a Monday' in AGENTS.md. My agent removed the line, shipped at 8:59 a.m., and git blame says Monday's 9 a.m. outage, ticket #4821, was mine."


def main():
    assert len(ENTRY) <= 200, f"entry too long: {len(ENTRY)} chars"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
