from expressions import Visitor, LiteralExpr, GroupingExpr, Expr, UnaryExpr
from token_type import TokenTypes 
from token import Token
from typing import Any, List
from runtime_error import RuntimeError
from stmt import StmtVisitor, ExprStmt, PrintStmt, Stmt
from enviroment import Enviroment

class Interpreter(Visitor, StmtVisitor):
    def __init__(self, runtime_error):
        self.runtime_error = runtime_error
        self.enviroment = Enviroment()

    def interpret(self, statements: List[Stmt])-> None:
        try:
            for statement in statements:
                self.execute(statement)
        except RuntimeError as error:
            self.runtime_error(error)

    def visit_literal(self, expr: LiteralExpr) -> Any:
        return expr.value

    def visit_grouping(self, expr: GroupingExpr) -> Any:
        return self.evaluate(expr.expr)

    def visit_unary(self, expr: UnaryExpr) -> Any:
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenTypes.MINUS:
                self.check_number_operand(expr.operator, right)
                return -float(right)
            case TokenTypes.BANG: 
                return not self.is_truthy(right)

        raise RuntimeError(expr.operator, "Unexpected unary operator.")

    def check_number_operand(self, operator: Token, operand: Any) -> None:
        if isinstance(operand, (float, int)): 
            return
        raise RuntimeError(operator, "Operand must be a number.")

    def check_number_operands(self, operator: Token, left: Any, right: Any) -> None:
        if isinstance(left, (float, int)) and isinstance(right, (float, int)):
            return
        raise RuntimeError(operator, "Operands must be numbers.")

    def is_truthy(self, object: Any) -> bool:
        return object is not None and bool(object)

    def is_equal(self, a: Any, b: Any) -> bool:
        if a is None and b is None:
            return True
        if a is None:
            return False
        return a == b

    def stringify(self, object: Any) -> str:
        if object is None:
            return "nil"

        if isinstance(object, (float, int)):
            text = str(object)
            if text.endswith(".0"):
                text = text[:-2]
            return text
        
        return str(object)
                
    def evaluate(self, expr: Expr) -> Any:
        return expr.accept(self)

    def execute(self, stmt: Stmt):
        stmt.accept(self)

    def visit_expr_stmt(self, stmt: ExprStmt):
        self.evaluate(stmt.expression)
        return None
    
    def visit_print_stmt(self, stmt: PrintStmt):
        value = self.evaluate(stmt.expression)
        print(self.stringify(value))
        return None

    def visit_binary(self, expr: Expr) -> Any:
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenTypes.MINUS:
                self.check_number_operands(expr.operator, left, right)
                return float(left) - float(right)
            case TokenTypes.SLASH:
                self.check_number_operands(expr.operator, left, right)
                return float(left) / float(right)
            case TokenTypes.STAR:
                self.check_number_operands(expr.operator, left, right)
                return float(left) * float(right)
            case TokenTypes.PLUS:
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return float(left) + float(right)
                if isinstance(left, str) and isinstance(right, str):
                    return left + right
                raise RuntimeError(expr.operator, "Operands must be two numbers or two strings.")
            case TokenTypes.GREATER:
                self.check_number_operands(expr.operator, left, right)
                return left > right
            case TokenTypes.GREATER_EQUAL:
                self.check_number_operands(expr.operator, left, right)
                return left >= right
            case TokenTypes.LESS:
                self.check_number_operands(expr.operator, left, right)
                return left < right
            case TokenTypes.LESS_EQUAL:
                self.check_number_operands(expr.operator, left, right)
                return left <= right
            case TokenTypes.BANG_EQUAL:
                return not self.is_equal(left, right)
            case TokenTypes.EQUAL_EQUAL:
                return self.is_equal(left, right)
            case _:
                raise RuntimeError(expr.operator, f"Unexpected operator: {expr.operator.type}")

