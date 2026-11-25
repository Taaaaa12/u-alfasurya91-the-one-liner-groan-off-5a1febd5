#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
Deterministic: the same joke every run, no network, no randomness,
no input files, no environment secrets.
"""

import os

JOKE = (
    "I told my GPS I needed space, so now it just says 'recalculating' "
    "every time I ask where we stand."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
