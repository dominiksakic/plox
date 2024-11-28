from token_type import TokenTypes 

class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"{self.type} {self.lexeme} {self.literal}"

    def to_string(self):
        return f"{self.type} {self.lexeme} {self.literal}"


