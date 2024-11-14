from token import Token 
from token_type import TokenTypes

class Scanner:
    tokens = []
    start = 0
    current = 0
    line = 1

    def __init__(self, source):
        self.source = source

    def scan_tokens(self): # Maybe add self to the method
        while(not self.is_at_end()):
            self.start = self.current
            #self.scan_token()
            self.current += 1 
            print(self.current)

        self.tokens.append(Token(TokenTypes.EOF, "", None, self.line))
        return self.tokens

    def is_at_end(self):
        return self.current >= len(self.source)


test = Scanner("Hello My name is Dominik")
test.scan_tokens();
print(test)
