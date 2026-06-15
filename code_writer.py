import os

class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, "w", encoding="utf-8")
        self.label_count = 0
        self.return_count = 0
        self.filename_base = os.path.basename(filename).replace(".asm", "")

        # Bootstrap: inicializa SP = 256
        self.write_init()

    def write_line(self, line):
        self.file.write(line + "\n")

    def write_init(self):
        self.write_line("// Bootstrap code")
        self.write_line("@256")
        self.write_line("D=A")
        self.write_line("@SP")
        self.write_line("M=D")
        self.write_line("// call Sys.init 0 sera implementado na etapa de sub-rotinas")

    def push_d(self):
        self.write_line("@SP")
        self.write_line("A=M")
        self.write_line("M=D")
        self.write_line("@SP")
        self.write_line("M=M+1")

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
            self.push_d()

        elif segment in segments:
            self.write_line(f"@{index}")
            self.write_line("D=A")
            self.write_line(f"@{segments[segment]}")
            self.write_line("A=D+M")
            self.write_line("D=M")
            self.push_d()

        elif segment == "temp":
            self.write_line(f"@{5 + index}")
            self.write_line("D=M")
            self.push_d()

        elif segment == "static":
            self.write_line(f"@{self.filename_base}.{index}")
            self.write_line("D=M")
            self.push_d()

        elif segment == "pointer":
            target = "THIS" if index == 0 else "THAT"
            self.write_line(f"@{target}")
            self.write_line("D=M")
            self.push_d()

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

        elif segment == "pointer":
            target = "THIS" if index == 0 else "THAT"
            self.write_line("@SP")
            self.write_line("AM=M-1")
            self.write_line("D=M")
            self.write_line(f"@{target}")
            self.write_line("M=D")

    def write_label(self, label):
        self.write_line(f"({label})")

    def write_goto(self, label):
        self.write_line(f"@{label}")
        self.write_line("0;JMP")

    def write_if(self, label):
        self.write_line("@SP")
        self.write_line("AM=M-1")
        self.write_line("D=M")
        self.write_line(f"@{label}")
        self.write_line("D;JNE")

    def write_function(self, function_name, n_locals):
        self.write_line(f"({function_name})")

        for _ in range(n_locals):
            self.write_line("@0")
            self.write_line("D=A")
            self.push_d()

    def write_call(self, function_name, n_args):
        return_label = f"RET_ADDRESS_{self.return_count}"
        self.return_count += 1

        # push return-address
        self.write_line(f"@{return_label}")
        self.write_line("D=A")
        self.push_d()

        # push LCL
        self.write_line("@LCL")
        self.write_line("D=M")
        self.push_d()

        # push ARG
        self.write_line("@ARG")
        self.write_line("D=M")
        self.push_d()

        # push THIS
        self.write_line("@THIS")
        self.write_line("D=M")
        self.push_d()

        # push THAT
        self.write_line("@THAT")
        self.write_line("D=M")
        self.push_d()

        # ARG = SP - nArgs - 5
        self.write_line("@SP")
        self.write_line("D=M")
        self.write_line(f"@{n_args + 5}")
        self.write_line("D=D-A")
        self.write_line("@ARG")
        self.write_line("M=D")

        # LCL = SP
        self.write_line("@SP")
        self.write_line("D=M")
        self.write_line("@LCL")
        self.write_line("M=D")

        # goto function
        self.write_line(f"@{function_name}")
        self.write_line("0;JMP")

        # return-address label
        self.write_line(f"({return_label})")

    def close(self):
        self.file.close()