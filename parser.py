class Parser:
    ARITHMETIC_COMMANDS = [
        "add", "sub", "neg",
        "eq", "gt", "lt",
        "and", "or", "not"
    ]

    def __init__(self, filename):
        self.commands = []
        self.current_command = None

        with open(filename, "r") as file:
            for line in file:
                line = line.split("//")[0].strip()

                if line:
                    self.commands.append(line.split())

    def has_more_commands(self):
        return len(self.commands) > 0

    def advance(self):
        if self.has_more_commands():
            self.current_command = self.commands.pop(0)
            return self.current_command
        return None

    def command_type(self):
        command = self.current_command[0]

        if command in self.ARITHMETIC_COMMANDS:
            return "C_ARITHMETIC"

        if command == "push":
            return "C_PUSH"

        if command == "pop":
            return "C_POP"

        if command == "label":
            return "C_LABEL"

        if command == "goto":
            return "C_GOTO"

        if command == "if-goto":
            return "C_IF"

        if command == "function":
            return "C_FUNCTION"

        if command == "call":
            return "C_CALL"

        if command == "return":
            return "C_RETURN"

        return None

    def arg1(self):
        command_type = self.command_type()

        if command_type == "C_ARITHMETIC":
            return self.current_command[0]

        if command_type == "C_RETURN":
            return None

        return self.current_command[1]

    def arg2(self):
        command_type = self.command_type()

        if command_type in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            return int(self.current_command[2])

        return None