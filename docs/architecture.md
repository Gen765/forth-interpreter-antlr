# Architecture

`forth.g4` defines a program as top-level numbers, definitions, and word calls.
Definition bodies additionally accept `if`/`else`/`endif`. ANTLR generates the
lexer, parser, and base visitor consumed by the handwritten modules.

`forth.interpret` creates a lexer and parser, replaces their default error
listeners, and visits the parse tree only when no syntax errors were recorded.
It prints accumulated output and converts runtime exceptions into user-facing
error lines.

`ForthInterpreter` owns:

- an integer stack;
- an output-line list;
- a call stack used by `recurse`;
- a dictionary of built-in callables; and
- a dictionary of user-defined parse-tree bodies.

User-defined words take precedence over built-ins. Calls push their name onto
the call stack and remove it in `finally`, preserving call-stack bookkeeping
when execution raises an error. Every call to `interpret` constructs a new
interpreter, so state does not persist.
