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
    def accept(self, Visitor[T]) -> T:
        pass
