from token import Token 
from token_type import TokenTypes

class Scanner:
    tokens = []
    start = 0
    current = 0
    line = 1

    def __init__(self, source):
        self.source = source

    def scan_tokens(self):
        while(not self.is_at_end()):
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenTypes.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        print(c)
        match c:
            case '(':
                pass 

    def is_at_end(self):
        return self.current >= len(self.source)


    def advance(self):
        temp_current = self.current
        self.current += 1

        return self.source[temp_current]

test = Scanner("Hello My name is Dominik")
token = test.scan_tokens();
print(token[0])
