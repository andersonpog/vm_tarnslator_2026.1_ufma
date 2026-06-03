from parser import Parser


def main():
    parser = Parser("tests/teste.vm")

    while parser.has_more_commands():
        command = parser.command()
        print(command)


if __name__ == "__main__":
    main()