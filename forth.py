"""Mini Forth Interpreter"""

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from forthLexer import forthLexer
from forthParser import forthParser
from visitor import ForthInterpreter


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Error de sintaxi a la línia {line}:{column}: {msg}")


def interpret(code):
    """
    Interpreta una cadena amb codi mini Forth i imprimeix la sortida.

    >>> interpret('2 3 + .')
    5
    """
    try:
        lexer = forthLexer(InputStream(code))
        lexer.removeErrorListeners()
        err = SyntaxErrorListener()
        lexer.addErrorListener(err)

        parser = forthParser(CommonTokenStream(lexer))
        parser.removeErrorListeners()
        parser.addErrorListener(err)

        tree = parser.program()

        if err.errors:
            for e in err.errors:
                print(e)
            return

        interp = ForthInterpreter()

        try:
            interp.visit(tree)
        except RuntimeError as e:
            out = interp.get_output()
            if out:
                print(out)
            print(f"Error: {e}")
            return

        out = interp.get_output()
        if out:
            print(out)

    except Exception as e:
        print(f"Error: {e}")
