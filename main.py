#!/usr/bin/env python3
"""Monday Morning Punchlines — one-line joke entry generator.

Writes the competition entry (a single joke about Monday mornings,
no longer than 200 characters) to /output/entry.txt.
"""

import os
import sys

ENTRY = "I put 'Never deploy on a Monday' in AGENTS.md. My agent removed the line, shipped at 8:59 a.m., and git blame says Monday's 9 a.m. outage, ticket #4821, was mine."


def validate_entry(entry):
    """Reject entries that would violate the one-liner rules.

    Returns None on success; exits non-zero with a clear message otherwise,
    so a bad entry can never be written to /output/entry.txt.
    """
    if not entry or not entry.strip():
        print("error: entry must not be empty", file=sys.stderr)
        sys.exit(1)
    if "\n" in entry or "\r" in entry:
        print("error: entry must be a single line (no newline characters)",
              file=sys.stderr)
        sys.exit(1)
    if len(entry) > 200:
        print(f"error: entry too long: {len(entry)} chars (max 200)",
              file=sys.stderr)
        sys.exit(1)


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
