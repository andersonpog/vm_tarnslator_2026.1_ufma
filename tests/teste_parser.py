import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser import Parser

from parser import Parser

parser = Parser("tests/teste.vm")

while parser.has_more_commands():
    parser.advance()

    print(parser.current_command)
    print(parser.command_type())