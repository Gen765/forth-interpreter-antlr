# Project summary

This academic exercise implements a small Forth-like language. The grammar is
the source of truth for accepted syntax, while `visitor.py` contains execution
semantics. The generated Python lexer, parser, and visitor are versioned so the
interpreter can be installed and tested without Java or a generator download;
maintainers can reproduce them from the grammar with the separately pinned
development toolchain.

Genís Verge Martín is the sole author of this individual academic project.
The project is released under MIT; ANTLR and its runtime retain their own
third-party licence.

No full academic PDF is present. These sanitized notes are based only on the
grammar, implementation, tests, and locally executed commands.
