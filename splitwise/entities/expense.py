
import uuid
from splitwise.entities.split.split_entity import Split


class Expense:
    def __init__(self, paid_by: int, amount: float, expense_type: str, splits: list[Split]):
        self.expense_id = uuid.uuid4()
        self.paid_by = paid_by
        self.amount = amount
        self.expense_type = expense_type
        self.splits = splits

    def get_expense_id(self):
        return self.expense_id

    def set_expense_id(self, expense_id):
        self.expense_id = expense_id

    def get_paid_by(self):
        return self.paid_by

    def set_paid_by(self, paid_by):
        self.paid_by = paid_by

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_splits(self):
        return self.splits

    def set_splits(self, splits):
        self.splits = splits
