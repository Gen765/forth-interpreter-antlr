import io
import unittest
import subprocess
import sys
from pathlib import Path
from contextlib import redirect_stdout

from forth import interpret


def run(source):
    output = io.StringIO()
    with redirect_stdout(output):
        interpret(source)
    return output.getvalue().strip()


class InterpreterTests(unittest.TestCase):
    def test_arithmetic_and_stack_output(self):
        self.assertEqual(run("2 3 + . 4 dup * ."), "5\n16")

    def test_definition_and_conditional(self):
        source = ": abs dup 0 < if 0 swap - endif ; -3 abs . 5 abs ."
        self.assertEqual(run(source), "3\n5")

    def test_recursive_definition(self):
        source = ": fact dup 2 < if drop 1 else dup 1 - recurse * endif ; 5 fact ."
        self.assertEqual(run(source), "120")

    def test_runtime_errors_are_reported(self):
        self.assertEqual(run("5 0 /"), "Error: divisió per zero!")
        self.assertEqual(run("unknown"), "Error: procediment 'unknown' no definit!")
        self.assertEqual(run("drop"), "Error: pila buida!")

    def test_syntax_errors_are_reported(self):
        self.assertIn("Error de sintaxi", run(": unfinished 1"))

    def test_cli_executes_inline_source(self):
        root = Path(__file__).resolve().parents[1]
        completed = subprocess.run(
            [sys.executable, "cli.py", "--code", "6 7 * ."],
            cwd=root, check=True, capture_output=True, text=True,
        )
        self.assertEqual(completed.stdout.strip(), "42")


if __name__ == "__main__":
    unittest.main()
