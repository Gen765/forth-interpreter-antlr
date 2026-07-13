# Forth Interpreter with ANTLR

A small interpreter for a Forth-like stack language. The versioned Python
lexer, parser, and visitor are generated from `forth.g4`; `visitor.py`
implements stack operations, user-defined words, conditionals, and recursion.
Keeping the generated runtime files in the repository means normal setup does
not download a generator or require Java.

## Verification Status

Fully verified.

The clean-environment generation and test commands are recorded in
[`docs/results.md`](docs/results.md).

## Pinned toolchain

- Python **3.14.0** (`.python-version`)
- ANTLR tool **4.13.2**
- `antlr4-python3-runtime==4.13.2`
- `antlr4-tools==0.2.2` for maintainers regenerating the parser
- A Java runtime is required only for regeneration, not installation or use.

The ANTLR generator and Python runtime intentionally use the same ANTLR
release.

## Clean setup

Windows PowerShell:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
.\.venv\Scripts\python.exe -m doctest tests/test.txt -v
```

Linux/macOS:

```sh
python3.14 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
.venv/bin/python -m doctest tests/test.txt -v
```

With the virtual environment activated, GNU Make provides the equivalent test
target:

```sh
make test
```

Maintainers can regenerate the versioned ANTLR files separately:

```sh
python -m pip install -r requirements-dev.txt
make generate
```

Regeneration may download the pinned ANTLR tool. Review the generated diff and
run `make test` before committing it.

## Usage

The generated files are included, so the interpreter is ready after installing
the runtime requirements.

```python
from forth import interpret

interpret("2 3 + .")
interpret(": double 2 * ; 5 double .")
```

Output:

```text
5
10
```

Runnable source examples are under [`examples/`](examples/).

The CLI accepts inline code, UTF-8 files, or piped standard input:

```sh
python cli.py --code ": square dup * ; 9 square ."
python cli.py examples/basics.forth
echo "6 7 * ." | python cli.py
```

## Supported language

- Signed decimal integers.
- Arithmetic: `+ - * / mod`.
- Comparisons: `< > = <> <= >=` (true is `-1`, false is `0`).
- Logic: `and or not`.
- Stack words: `dup drop swap over rot 2dup 2drop 2swap 2over`.
- Output: `.` and `.s`.
- Definitions: `: name ... ;`.
- `if ... else ... endif` inside definitions.
- Recursive calls by word name or `recurse`.
- Non-nested `( ... )` comments.

`interpret(source)` creates a fresh stack and dictionary on every call and
prints output. Syntax and runtime errors are reported as text instead of being
raised to the caller.

## Documentation

- [`docs/project-summary.md`](docs/project-summary.md)
- [`docs/architecture.md`](docs/architecture.md)
- [`docs/results.md`](docs/results.md)

## Authorship and licensing

Genís Verge Martín is the sole author of the grammar, interpreter, tests and
generated parser sources. The project is released under the [MIT License](LICENSE).
ANTLR remains third-party software under its own licence; see
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Limitations

- No loops or persistent REPL state.
- Conditionals are grammar-valid only inside definitions.
- Comments do not nest.
- Integer division uses Python floor division.
- Runtime errors can leave values already popped by the failing operation;
  each `interpret` call is isolated, so this does not affect later calls.
