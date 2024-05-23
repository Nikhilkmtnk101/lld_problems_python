from splitwise.expense.expense import Expense
from splitwise.splits.percent_split import PercentSplit
from splitwise.splits.split import Split
from splitwise.user.user import User


class PercentExpense(Expense):
    def __init__(self, amount: float, paid_by: User, splits: list[Split]):
        super(PercentExpense, self).__init__(amount, paid_by, splits)

    def validate(self):
        total_percent = 0

        for split in self.splits:
            if not isinstance(split, PercentSplit):
                return False
            total_percent = total_percent + split.get_percent()

        return total_percent == 100.0
