from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any

T = TypeVar('T')

class StmtVisitor(Generic[T], ABC):
    @abstractmethod
    def visit_expr_stmt(self,expr) -> T:
        pass
        
    @abstractmethod
    def visit_print_stmt(self,expr) -> T:
        pass 

    @abstractmethod
    def visit_var_stmt(self,expr) -> T:
        pass 

class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor: StmtVisitor[T]) -> T:
        pass

class ExprStmt(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor: StmtVisitor[T]) -> T:
        return visitor.visit_expr_stmt(self)


class PrintStmt(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor: StmtVisitor[T]) -> T:
        return visitor.visit_print_stmt(self)

class VarStmt(Stmt):
    def __init__(self, name, initializer):
        self.name = name
        self.expression = expression

    def accept(self, visitor: StmtVisitor[T]) -> T:
        return visitor.visit_var_stmt(self)

