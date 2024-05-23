from splitwise.expense.expense import Expense
from splitwise.splits.equal_split import EqualSplit
from splitwise.splits.split import Split
from splitwise.user.user import User


class EqualExpense(Expense):
    def __init__(self, amount: float, paid_by: User, splits: list[Split]):
        super(EqualExpense, self).__init__(amount, paid_by, splits)

    def validate(self):
        for split in self.splits:
            if not isinstance(split, EqualSplit):
                return False

        return True
