import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from code_writer import CodeWriter

writer = CodeWriter("tests/teste_temp.asm")

writer.write_push("temp", 2)
writer.write_pop("temp", 3)

writer.close()