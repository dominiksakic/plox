from expressions import Visitor, Expr, BinaryExpr, GroupingExpr, LiteralExpr, UnaryExpr
from token import Token

class AstPrinter(Visitor):
    def print(self, expr: Expr) -> str:
        return expr.accept(self)

    def visit_binary(self, expr: BinaryExpr) -> str:
        return f"({expr.operator} {expr.left.accept(self)} {expr.right.accept(self)})"

    def visit_grouping(self, expr: GroupingExpr) -> str:
        return f"(group {expr.expr.accept(self)})"

    def visit_literal(self, expr: LiteralExpr) -> str:
        return str(expr.value)

    def visit_unary(self, expr: UnaryExpr) -> str:
        return f"({expr.operator} {expr.right.accept(self)})"

if __name__ == "__main__":
    # For Testing purpose 
    expr = BinaryExpr(
        left=LiteralExpr(1),
        operator="+",
        right=LiteralExpr(2)
    )

    expr2 = BinaryExpr(
    UnaryExpr(
        operator=Token("MINUS", "-", None, 1),
        right=LiteralExpr(123)
    ),
    operator=Token("STAR", "*", None, 1),
    right=GroupingExpr(
        LiteralExpr(45.67)
    )
)

