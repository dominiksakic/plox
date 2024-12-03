from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any
from token import Token 

T = TypeVar('T')

class Visitor(Generic[T], ABC):
    @abstractmethod
    def visit_binary(self,expr:'BinaryExpr') -> T:
        pass

    @abstractmethod
    def visit_grouping(self,expr:'GroupingExpr') -> T:
        pass

    @abstractmethod
    def visit_literal(self,expr:'LiteralExpr') -> T:
        pass

    @abstractmethod
    def visit_unary(self,expr:'UnaryExpr') -> T:
        pass

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor[T]) -> T:
        pass

class BinaryExpr(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.operator = operator
        self.right= right

    def accept(self, visitor: Visitor[T]) -> T:
        return visitor.visit_binary(self)

class GroupingExpr(Expr):
    def __init__(self, expr: Expr):
        self.expr = expr

    def accept(self, visitor: Visitor[T]) -> T:
        return visitor.visit_grouping(self)

class LiteralExpr(Expr):
    def __init__(self, value: Any):
        self.value= value 

    def accept(self, visitor: Visitor[T]) -> T:
        return visitor.visit_literal(self)

class UnaryExpr(Expr):
    def __init__(self, operator: Token, right: Expr):
        self.operator = operator
        self.right = right

    def accept(self, visitor: Visitor[T]) -> T:
        return visitor.visit_unary(self)
