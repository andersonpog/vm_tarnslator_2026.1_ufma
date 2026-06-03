class Parser:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.commands = []

            for line in file:
                line = line.split("//")[0].strip()

                if line:
                    self.commands.append(line.split())

    def has_more_commands(self):
        return len(self.commands) > 0

    def command(self):
        if self.has_more_commands():
            return self.commands.pop(0)
        return None