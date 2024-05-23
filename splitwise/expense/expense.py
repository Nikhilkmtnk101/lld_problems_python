from abc import ABC, abstractmethod

from splitwise.splits.split import Split
from splitwise.user.user import User


class Expense(ABC):
    def __init__(self, amount: float, paid_by: User, splits: list[Split]):
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits

    def set_amount(self, amount: float):
        self.amount = amount

    def get_amount(self) -> float:
        return self.amount

    def set_paid_by(self, paid_by: User):
        self.paid_by = paid_by

    def get_paid_by(self) -> User:
        return self.paid_by

    def set_splits(self, splits: list[Split]):
        self.splits = splits

    def get_splits(self) -> list[Split]:
        return self.splits

    @abstractmethod
    def validate(self):
        pass
