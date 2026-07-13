# Verification results

Verified in a newly created `.venv` on Windows 10.

## Environment

```text
Python 3.14.0
antlr4-python3-runtime==4.13.2
```

The environment was created and populated with:

```text
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Dependency installation completed with exit code 0.

The versioned ANTLR Python files were used directly; neither Java nor a
generator download was required for this runtime verification.

## Regeneration

Maintainers install the separate development dependencies before regenerating:

```text
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\antlr4.exe -v 4.13.2 -Dlanguage=Python3 -no-listener -visitor forth.g4
```

The generated lexer, parser, and visitor are reviewed and committed so normal
users do not depend on a dynamic ANTLR download.

The generator command was previously validated with `antlr4-tools==0.2.2`:

```text
.\.venv\Scripts\antlr4.exe -v 4.13.2 -Dlanguage=Python3 -no-listener -visitor forth.g4
```

Generation completed with exit code 0 and no output.

## Tests

```text
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

Result: 6 tests passed, including the command-line interface regression test.

```text
.\.venv\Scripts\python.exe -m doctest tests/test.txt -v
```

Result: 29 doctest examples passed.

The Makefile generation path was also validated from a
virtual-environment-activated shell:

```text
mingw32-make generate test
```

Generation and both test suites completed successfully.

## Example

```text
.\.venv\Scripts\python.exe examples\run_example.py
5
10
```

All final generation, test, and example commands exited with code 0.
