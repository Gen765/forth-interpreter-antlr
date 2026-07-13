"""Command-line interface for the Forth subset interpreter."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from forth import interpret


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--code", help="Interpret one source string")
    source.add_argument("file", nargs="?", type=Path, help="Read source from a UTF-8 file")
    args = parser.parse_args()
    if args.code is not None:
        text = args.code
    elif args.file is not None:
        text = args.file.read_text(encoding="utf-8")
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.error("provide --code, a file, or piped standard input")
    interpret(text)


if __name__ == "__main__":
    main()
