class Enviroment:
    def __init__(self):
        self.values = {} 

    def define(self, name, value):
        self.values[name] = value
        return None

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        raise RuntimeError(name, f"Undefined variable '{name.lexeme}'.")

class RuntimeError(Exception):
    def __init__(self, token, message):
        super().__init__(f"[Line {token.line}] {message}")
        self.token = token
        self.message = message

