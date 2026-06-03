class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, "w")
        self.label_count = 0
        self.filename_base = "Static"

    def write_line(self, line):
        self.file.write(line + "\n")

    def write_comparison(self, jump_command):
        true_label = f"TRUE_{self.label_count}"
        end_label = f"END_{self.label_count}"
        self.label_count += 1

        self.write_line("@SP")
        self.write_line("AM=M-1")
        self.write_line("D=M")
        self.write_line("A=A-1")
        self.write_line("D=M-D")

        self.write_line(f"@{true_label}")
        self.write_line(f"D;{jump_command}")

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
            self.write_comparison("JEQ")

        elif command == "gt":
            self.write_comparison("JGT")

        elif command == "lt":
            self.write_comparison("JLT")

    def write_push(self, segment, index):
        segments = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT"
        }

        if segment == "constant":
            self.write_line(f"@{index}")
            self.write_line("D=A")
            self.write_line("@SP")
            self.write_line("A=M")
            self.write_line("M=D")
            self.write_line("@SP")
            self.write_line("M=M+1")

        elif segment in segments:
            self.write_line(f"@{index}")
            self.write_line("D=A")
            self.write_line(f"@{segments[segment]}")
            self.write_line("A=D+M")
            self.write_line("D=M")
            self.write_line("@SP")
            self.write_line("A=M")
            self.write_line("M=D")
            self.write_line("@SP")
            self.write_line("M=M+1")

        elif segment == "temp":
            self.write_line(f"@{5 + index}")
            self.write_line("D=M")
            self.write_line("@SP")
            self.write_line("A=M")
            self.write_line("M=D")
            self.write_line("@SP")
            self.write_line("M=M+1")

        elif segment == "static":
            self.write_line(f"@{self.filename_base}.{index}")
            self.write_line("D=M")
            self.write_line("@SP")
            self.write_line("A=M")
            self.write_line("M=D")
            self.write_line("@SP")
            self.write_line("M=M+1")

    def write_pop(self, segment, index):
        segments = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT"
        }

        if segment in segments:
            self.write_line(f"@{index}")
            self.write_line("D=A")
            self.write_line(f"@{segments[segment]}")
            self.write_line("D=D+M")

            self.write_line("@R13")
            self.write_line("M=D")

            self.write_line("@SP")
            self.write_line("AM=M-1")
            self.write_line("D=M")

            self.write_line("@R13")
            self.write_line("A=M")
            self.write_line("M=D")

        elif segment == "temp":
            self.write_line("@SP")
            self.write_line("AM=M-1")
            self.write_line("D=M")
            self.write_line(f"@{5 + index}")
            self.write_line("M=D")

        elif segment == "static":
            self.write_line("@SP")
            self.write_line("AM=M-1")
            self.write_line("D=M")
            self.write_line(f"@{self.filename_base}.{index}")
            self.write_line("M=D")

    def close(self):
        self.file.close()