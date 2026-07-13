import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from forth import interpret


SOURCE = Path(__file__).with_name("basics.forth")
interpret(SOURCE.read_text(encoding="utf-8"))
