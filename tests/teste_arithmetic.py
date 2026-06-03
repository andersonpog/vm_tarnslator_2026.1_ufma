import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from code_writer import CodeWriter


writer = CodeWriter("tests/teste_arithmetic.asm")

writer.write_arithmetic("add")
writer.write_arithmetic("sub")
writer.write_arithmetic("and")
writer.write_arithmetic("or")

writer.close()