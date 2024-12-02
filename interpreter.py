from typing import Any
from expressions import Visitor, LiteralExpr, GroupingExpr, Expr

class Interpreter(Visitor):
    def visit_literal(self, expr: LiteralExpr) -> Any:
        return expr.value

    def visit_grouping(self, expr: GroupingExpr) -> Any:
        return self.evaluate(expr.expr)
    
    def evaluate(self, expr: Expr) -> Any:
        return expr.accept(self)
