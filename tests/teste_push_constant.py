import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from code_writer import CodeWriter

writer = CodeWriter("tests/teste_push_constant.asm")

writer.write_push("constant", 7)
writer.write_push("constant", 8)

writer.close()