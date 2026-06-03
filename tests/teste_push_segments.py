import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from code_writer import CodeWriter

writer = CodeWriter("tests/teste_push_segments.asm")

writer.write_push("local", 0)
writer.write_push("argument", 1)
writer.write_push("this", 2)
writer.write_push("that", 3)

writer.close()