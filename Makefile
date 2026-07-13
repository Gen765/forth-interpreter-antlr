PYTHON ?= python
ANTLR4 ?= antlr4
ANTLR_VERSION := 4.13.2
GENERATED := forthLexer.py forthParser.py forthVisitor.py

.PHONY: all generate test clean

all: test

generate:
	$(ANTLR4) -v $(ANTLR_VERSION) -Dlanguage=Python3 -no-listener -visitor forth.g4

test:
	$(PYTHON) -m unittest discover -s tests -p "test_*.py" -v
	$(PYTHON) -m doctest tests/test.txt -v

clean:
ifeq ($(OS),Windows_NT)
	cmd /C del /Q forth.interp forth.tokens forthLexer.interp forthLexer.tokens 2>NUL
	cmd /C if exist __pycache__ rmdir /S /Q __pycache__
	cmd /C if exist tests\__pycache__ rmdir /S /Q tests\__pycache__
else
	$(RM) forth.interp forth.tokens forthLexer.interp forthLexer.tokens
	$(RM) -r __pycache__ tests/__pycache__
endif
