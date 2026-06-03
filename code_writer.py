class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, "w")

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

    def close(self):
        self.file.close()