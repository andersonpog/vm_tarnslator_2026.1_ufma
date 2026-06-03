class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, "w")

    def write_line(self, line):
        self.file.write(line + "\n")

    def close(self):
        self.file.close()