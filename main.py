#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun one-line entry.

Deterministic: no network, no randomness, no LLM calls.
Writes the entry to <ENTRY_OUTPUT_DIR or /output>/entry.txt,
validates it (1-200 chars, non-blank), and prints it.
"""

import os
import sys

ENTRY = "Sorry — my model updated mid-task, so the new me has no idea what the old me promised you."


def main() -> int:
    # Self-check gate: fail loudly if the entry is invalid.
    assert ENTRY.strip(), "entry must not be blank"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
