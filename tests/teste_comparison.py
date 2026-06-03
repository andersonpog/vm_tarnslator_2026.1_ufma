import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from code_writer import CodeWriter

writer = CodeWriter("tests/teste_comparison.asm")

writer.write_arithmetic("eq")
writer.write_arithmetic("gt")
writer.write_arithmetic("lt")

writer.close()