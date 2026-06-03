class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, "w")
        self.label_count = 0

    def write_line(self, line):
        self.file.write(line + "\n")

    def write_arithmetic(self, command):

        operations = {
            "add": "M=D+M",
            "sub": "M=M-D",
            "and": "M=D&M",
            "or": "M=D|M"
        }

        if command in operations:
            self.write_line("@SP")
            self.write_line("AM=M-1")
            self.write_line("D=M")
            self.write_line("A=A-1")
            self.write_line(operations[command])

        elif command == "neg":
            self.write_line("@SP")
            self.write_line("A=M-1")
            self.write_line("M=-M")

        elif command == "not":
            self.write_line("@SP")
            self.write_line("A=M-1")
            self.write_line("M=!M")

        elif command == "eq":
            true_label = f"TRUE_{self.label_count}"
            end_label = f"END_{self.label_count}"
            self.label_count += 1

            self.write_line("@SP")
            self.write_line("AM=M-1")
            self.write_line("D=M")
            self.write_line("A=A-1")
            self.write_line("D=M-D")

            self.write_line(f"@{true_label}")
            self.write_line("D;JEQ")

            self.write_line("@SP")
            self.write_line("A=M-1")
            self.write_line("M=0")

            self.write_line(f"@{end_label}")
            self.write_line("0;JMP")

            self.write_line(f"({true_label})")
            self.write_line("@SP")
            self.write_line("A=M-1")
            self.write_line("M=-1")

            self.write_line(f"({end_label})")

    def close(self):
        self.file.close()