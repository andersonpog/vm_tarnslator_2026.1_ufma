import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from code_writer import CodeWriter

writer = CodeWriter("tests/teste_pop_segments.asm")

writer.write_pop("local", 0)
writer.write_pop("argument", 1)
writer.write_pop("this", 2)
writer.write_pop("that", 3)

writer.close()