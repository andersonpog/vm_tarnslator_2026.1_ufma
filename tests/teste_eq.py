import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from code_writer import CodeWriter

writer = CodeWriter("tests/teste_eq.asm")

writer.write_arithmetic("eq")

writer.close()