import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from code_writer import CodeWriter

writer = CodeWriter("tests/teste_static.asm")

writer.write_push("static", 5)
writer.write_pop("static", 6)

writer.close()