from expressions import Visitor, Expr, BinaryExpr, GroupingExpr, LiteralExpr, UnaryExpr

class AstPrinter(Visitor):
    def print(self, expr: Expr) -> str:
        return expr.accept(self)

    def visit_binary(self, expr: BinaryExpr) -> str:
        return f"({expr.operator} {expr.left.accept(self)} {expr.right.accept(self)})"

    def visit_grouping(self, expr: GroupingExpr) -> str:
        return f"{expr.expr.accept(self)}"

    def visit_literal(self, expr: LiteralExpr) -> str:
        return str(expr.value)

    def visit_unary(self, expr: UnaryExpr) -> str:
        return f"{expr.operator} {expr.expr.accept(self)"
