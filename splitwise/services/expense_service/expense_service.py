from abc import ABC, abstractmethod

from splitwise.entities.expense import Expense
from splitwise.entities.split.split_entity import Split


class ExpenseService(ABC):

    @abstractmethod
    def create_expense(self, paid_by_user_id: int, amount: float, splits: list[Split]) -> Expense:
        pass

    @abstractmethod
    def validate_expense(self, paid_by_user_id: int, amount: float, splits: list[Split]) -> bool:
        pass
