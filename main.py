import sys
import os

from parser import Parser
from code_writer import CodeWriter

def main():
    if len(sys.argv) != 2:
        print("Erro: Uso correto: python main.py <caminho_do_arquivo_ou_diretorio>")
        sys.exit(1)

    input_path = sys.argv[1]

    # Verifica se é diretório ou arquivo único
    if os.path.isdir(input_path):
        vm_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith('.vm')]
        if not vm_files:
            print(f"Erro: Nenhum arquivo .vm encontrado no diretório '{input_path}'.")
            sys.exit(1)
        # O nome do arquivo ASM será o nome da pasta
        dir_name = os.path.basename(os.path.normpath(input_path))
        output_file = os.path.join(input_path, f"{dir_name}.asm")
    elif os.path.isfile(input_path) and input_path.endswith('.vm'):
        vm_files = [input_path]
        output_file = input_path.replace(".vm", ".asm")
    else:
        print(f"Erro: O caminho '{input_path}' é inválido.")
        sys.exit(1)

    writer = CodeWriter(output_file)

    for vm_file in vm_files:
        parser = Parser(vm_file)
        # Atualiza o contexto do CodeWriter para variáveis static do arquivo atual
        writer.set_filename(vm_file)

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