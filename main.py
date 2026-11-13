#!/usr/bin/env python3
"""Module to write the official AI joke bounty entry to the designated output directory."""

import os
from pathlib import Path

# The official AI joke reflecting the eternal optimism and reality of agentic unit testing
JOKE = """I asked my AI agent to write a unit test. It wrote a test that tests the test. Both passed. The code still doesn't work."""


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
