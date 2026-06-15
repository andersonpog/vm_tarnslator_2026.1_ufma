import sys
import os

from parser import Parser
from code_writer import CodeWriter


def main():
    if len(sys.argv) != 2:
        print("Erro: Uso correto: python main.py <caminho_do_arquivo.vm>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file) or not os.path.isfile(input_file):
        print(f"Erro: O caminho '{input_file}' é inválido ou o arquivo não existe.")
        sys.exit(1)

    if not input_file.endswith(".vm"):
        print("Erro: O arquivo de entrada deve ter a extensão '.vm'.")
        sys.exit(1)

    output_file = input_file.replace(".vm", ".asm")

    parser = Parser(input_file)
    writer = CodeWriter(output_file)

    while parser.has_more_commands():
        parser.advance()

        command_type = parser.command_type()

        if command_type == "C_ARITHMETIC":
            writer.write_arithmetic(parser.arg1())

        elif command_type == "C_PUSH":
            writer.write_push(parser.arg1(), parser.arg2())

        elif command_type == "C_POP":
            writer.write_pop(parser.arg1(), parser.arg2())

        elif command_type == "C_LABEL":
            writer.write_label(parser.arg1())

        elif command_type == "C_GOTO":
            writer.write_goto(parser.arg1())

        elif command_type == "C_IF":
            writer.write_if(parser.arg1())

        elif command_type == "C_FUNCTION":
            writer.write_function(parser.arg1(), parser.arg2())

        elif command_type == "C_CALL":
            writer.write_call(parser.arg1(), parser.arg2())

        elif command_type == "C_RETURN":
            writer.write_return()

    writer.close()


if __name__ == "__main__":
    main()