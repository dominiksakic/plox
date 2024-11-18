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
                self.add_token(TokenTypes.LEFT_PAREN) 
            case ')':
                self.add_token(TokenTypes.RIGHT_PAREN)
            case '{':
                self.add_token(TokenTypes.LEFT_BRACE)
            case '}':
                self.add_token(TokenTypes.RIGHT_BRACE)
            case ',':
                self.add_token(TokenTypes.COMMA)
            case '.':
                self.add_token(TokenTypes.DOT)
            case '-':
                self.add_token(TokenTypes.MINUS)
            case '+':
                self.add_token(TokenTypes.PLUS)
            case ';':
                self.add_token(TokenTypes.SEMICOLON)
            case '*':
                self.add_token(TokenTypes.STAR)

    def is_at_end(self):
        return self.current >= len(self.source)


    def advance(self):
        temp_current = self.current
        self.current += 1

        return self.source[temp_current]

    def add_token(self, type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))

test = Scanner("Hello My name is Dominik (")
token = test.scan_tokens();
print(test.tokens[0].to_string())
