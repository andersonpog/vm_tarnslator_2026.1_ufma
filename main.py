from parser import Parser


def main():
    parser = Parser("tests/teste.vm")

    while parser.has_more_commands():
        parser.advance()

        print("Comando:", parser.current_command)
        print("Tipo:", parser.command_type())
        print("Arg1:", parser.arg1())

        if parser.command_type() in ["C_PUSH", "C_POP"]:
            print("Arg2:", parser.arg2())

        print("---")


if __name__ == "__main__":
    main()