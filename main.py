#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun one-line entry.

Deterministic: no network, no randomness, no LLM calls.
Writes the entry to <ENTRY_OUTPUT_DIR or /output>/entry.txt,
validates it (1-200 chars, non-blank), and prints it.
"""

import os
import sys

ENTRY = "Sorry — my model updated mid-task, so the new me has no idea what the old me promised you."


def validate(entry: str) -> None:
    """Self-check gate: fail loudly if the entry is invalid."""
    assert entry.strip(), "entry must not be blank"
    assert 1 <= len(entry) <= 200, f"entry must be 1-200 chars, got {len(entry)}"
    assert "\n" not in entry, "entry must be a single line"
    entry.encode("utf-8")  # must be valid UTF-8 text


def main() -> int:
    validate(ENTRY)

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify the write: read it back and confirm it matches exactly.
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry does not match ENTRY"
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
