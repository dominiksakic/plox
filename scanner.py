from token import Token 
from token_type import TokenTypes
from main import Plox 

class Scanner:
    tokens = []
    start = 0
    current = 0
    line = 1

    keywords = {
        "and": TokenTypes.AND,
        "class": TokenTypes.CLASS,
        "else": TokenTypes.ELSE,
        "false": TokenTypes.FALSE,
        "for": TokenTypes.FOR,
        "fun": TokenTypes.FUN,
        "if": TokenTypes.IF,
        "nil": TokenTypes.NIL,
        "or": TokenTypes.OR,
        "print": TokenTypes.PRINT,
        "return": TokenTypes.RETURN,
        "super": TokenTypes.SUPER,
        "this": TokenTypes.THIS,
        "true": TokenTypes.TRUE,
        "var": TokenTypes.VAR,
        "while": TokenTypes.WHILE
    }

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
            case '!':
                self.add_token(self.match('=') if TokenTypes.BANG_EQUAL else TokenTypes.BANG)
            case '=':
                self.add_token(self.match('=') if TokenTypes.EQUAL_EQUAL else TokenTypes.EQUAL)
            case '<':
                self.add_token(self.match('=') if TokenTypes.LESS_EQUAL else TokenTypes.LESS)
            case '>':
                self.add_token(self.match('=') if TokenTypes.GREATER_EQAUL else TokenTypes.GREATER)
            case '/':
                if(self.match('/')):
                    while(self.peek() != '\n' and not self.is_at_end()): self.advance()
                else: 
                    self.add_token(TokenTypes.SLASH)
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass
            case '\n':
                self.line += 1
            case '"':
                self.string()
            case _:
                if(self.is_digit(c)):
                    self.number()
                elif (self.is_alpha(c)):
                    self.identifier()
                else:
                    Plox.error(self.line, "Unexpected character.")

    def identifier(self):
        while(self.is_alpha_numeric(self.peek())): 
            self.advance()
            
        text = self.source[self.start: self.current]
        type = self.keywords[text]
        
        if(type == None): 
            type = TokenTypes.identifier

        self.add_token(type)

    def number(self):
        while(self.is_digit(self.peek())):
            self.advance()

        if(self.peek() == '.' and self.is_digit(self.peek_next())):
            self.advance()
            while(self.is_digit(self.peek())):
                self.advance()

        value = self.source[self.start:self.current]
        self.add_token(TokenTypes.NUMBER, value)

    def string(self):
        while(self.peek() != '"' and not self.is_at_end()):
            
            if(self.peek() == '\n'): 
                self.line += 1

            self.advance()
        
        if (self.is_at_end()):
            Lox.error(self.line, "Unterminated String")
            return Null

        self.advance()

        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenTypes.STRING, value)


    def match(self, expected):
        if(self.is_at_end()): return False
        if(self.source[self.current]!= expected) : return False

        self.current += 1
        return True

    def peek(self):
        if(self.is_at_end()): return '\0'
        return self.source[self.current]

    def peek_next(self):
        if(self.current + 1 >= len(self.source)): return '\0'
        return self.source[self.current + 1]

    def is_alpha(self, c):
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'

    def is_alpha_numeric(self, c):
        return self.is_alpha(c) or self.is_digit(c)

    def is_digit(self, char):
        is_digit = char >= '0' and char <='9' 
        return is_digit

    def is_at_end(self):
        return self.current >= len(self.source)


    def advance(self):
        temp_current = self.current
        self.current += 1

        return self.source[temp_current]

    def add_token(self, type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))

test = Scanner('and')
token = test.scan_tokens();
print(test.tokens[0].to_string())
