from abc import ABC
from typing import TypeVar, Generic, Any

T = TypeVar('T')

class Visitor(Generic[T], ABC):
    @abstractmethod
    def visit_expr_stmt(self,expr) -> T:
        pass
        
class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor[T]) -> T:
        pass

class ExprStmt(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor: Visitor[T]) -> T:
        return visitor.visit_expr_stmt(self)


class PrintStmt(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor: Visitor[T]) -> T:
        return visitor.visit_expr_stmt(self)
