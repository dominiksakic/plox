from token_type import TokenTypes
from expressions import BinaryExpr, UnaryExpr, LiteralExpr, GroupingExpr

class Parser():
    def __init__(self, tokens, error_handler):
        self.tokens = tokens
        self.error_handler = error_handler
        self.current = 0

    def parse(self):
        try:
            return self.expression()
        except ParseError:
            return None 

    def expression(self):
        return self.equality()

    def equality(self):
        expr = self.comparison() 

        while(self.match(TokenTypes.BANG_EQUAL, TokenTypes.BANG_EQUAL)):
            operator = self.previous()
            right = self.comparison()
            expr = BinaryExpr(expr, operator, right) 

        return expr

    def comparison(self):
        expr = self.term()

        while(self.match(TokenTypes.GREATER, TokenTypes.GREATER_EQUAL, TokenTypes.LESS, TokenTypes.LESS_EQUAL)):
            operator = self.previous()
            right = self.term()
            expr = BinaryExpr(expr, operator, right)

        return expr 
    
    def term(self):
        expr = self.factor()

        while(self.match(TokenTypes.MINUS, TokenTypes.PLUS)):
            operator = self.previous()
            right = self.factor()
            expr = BinaryExpr(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while(self.match(TokenTypes.SLASH, TokenTypes.STAR)):
            operator = self.previous()
            right = self.unary()
            expr = BinaryExpr(expr, operator, right)

        return expr

    def unary(self):
        if(self.match(TokenTypes.BANG, TokenTypes.MINUS)):
            operator = self.previous()
            right = self.unary()
            return  UnaryExpr(operator, right)

        return self.primary()
    
    def primary(self):
        if(self.match(TokenTypes.FALSE)): 
            return LiteralExpr(False)
        if(self.match(TokenTypes.TRUE)):
            return LiteralExpr(True)
        if(self.match(TokenTypes.NIL)):
            return LiteralExpr(None)

        if(self.match(TokenTypes.NUMBER, TokenTypes.STRING)):
            return LiteralExpr(self.previous().literal)

        if(self.match(TokenTypes.LEFT_PAREN)):
            expr = self.expression()
            self.consume(TokenTypes.RIGHT_PAREN, "Expect ')' after expression.")
            return GroupingExpr(expr)

        raise self.error(self.peek(), "Expect Expression.")

    def match(self, *types):
        for type_ in types:
            
            if(self.check(type_)):
                self.advance()
                return True

        return False

    def consume(self, type, message):
        if(self.check(type)) : return self.advance()

        raise self.error(self.peek(), message)

    def check(self, type):
        if(self.is_at_end()):
            return False

        return self.peek().type == type

    def advance(self):
        if(not self.is_at_end()):
            self.current += 1

        return self.previous()

    def is_at_end(self):
        return self.peek().type == TokenTypes.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]
    
    def error(self, token, message):
        self.error_handler(token, message)
        return ParseError(message)

    def report_error(self,token ,message):
        if token.type == TokenTypes.EOF:
            print(f"[line {token.line}] Error at end: {message}")
        else:
            print(f"[line {token.line}] Error at '{token.lexeme}': {message}")
    
    def synchronize(self):
        self.advance()

        while not self.is_at_end():
            if self.previous().type == TokenTypes.SEMICOLON:
                return

            if self.peek().type in {
                TokenTypes.CLASS,
                TokenTypes.FUN,
                TokenTypes.VAR,
                TokenTypes.FOR,
                TokenTypes.IF,
                TokenTypes.WHILE,
                TokenTypes.PRINT,
                TokenTypes.RETURN,
            }:
                return

            self.advance()
    
class ParseError(RuntimeError):
    pass
