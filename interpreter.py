from typing import Any
from expressions import Visitor, LiteralExpr, GroupingExpr, Expr, UnaryExpr
from token_type import TokenTypes 

class Interpreter(Visitor):
    def visit_literal(self, expr: LiteralExpr) -> Any:
        return expr.value

    def visit_grouping(self, expr: GroupingExpr) -> Any:
        return self.evaluate(expr.expr)

    def visit_unary(self, expr: UnaryExpr) -> Any:
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenTypes.MINUS:
                return -float(right)
            case TokenTypes.BANG:
                return not self.is_truthy(right)

        return None
    
    def is_truthy(self, object: Any) -> bool:
        if object is None:
            return False
        
        if isinstance(object, bool): 
            return object

        return True

    def is_equal(self, a: Any, b: Any) -> bool:
        if a is None and b is None:
            return True
        if a is None:
            return False

        return a == b

    def evaluate(self, expr: Expr) -> Any:
        return expr.accept(self)

    def visit_binary(self, expr: Expr) -> Any:
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        match expr.operator.type:
            case TokenTypes.MINUS:
                return float(left) - float(right)
            case TokenTypes.SLASH:
                return float(left) / float(right)
            case TokenTypes.STAR:
                return float(left) * float(right)
            case TokenTypes.PLUS:
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return float(left) + float(right)
                if isinstance(left, str) and isinstance(right, str):
                    return left + right
            case TokenTypes.GREATER:
                return left > right
            case TokenTypes.GREATER_EQUAL:
                return left >= right
            case TokenTypes.LESS:
                return left < right
            case TokenTypes.LESS_EQUAL:
                return left <= right
            case TokenTypes.BANG_EQUAL:
                return not self.is_equal(left, right)
            case TokenTypes.EQUAL_EQUAL:
                return self.is_equal(left, right)

        return None

    
