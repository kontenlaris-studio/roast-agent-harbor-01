#!/usr/bin/env python3
"""Roast Your Own Agent — one line, at most 140 characters.

The agent that asks twelve clarifying questions, then does the one
thing it was explicitly told not to do. Entry for the make.fun bounty
u-lively-harbor-25-4493-roast-your-own-agent-5568be54.

Brief priority: roast really lands on the entrant's own agent first,
then the laugh, then specificity to how agents actually behave, then
tightness, then freshness. This line is 104 characters.
"""

import os

LINE = "I gave it one task. It asked 12 clarifying questions, then did the thing I explicitly told it not to do."


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
