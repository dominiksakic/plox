from token_type import TokenTypes
class Parser():
    current = 0

    def __init__(self, tokens):
        self.tokens = tokens

    def check(self, type):
        if(self.is_at_end()):
            return False

        return self.peek().type == type

    def advance(self):
        if(not self.is_at_end(self)):
            self.current += 1

        return self.previous()

    def is_at_end(self):
        return self.peek().type == TokenTypes.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]
