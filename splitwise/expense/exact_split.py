from splitwise.expense.expense import Expense
from splitwise.splits.exact_split import ExactSplit
from splitwise.splits.split import Split
from splitwise.user.user import User


class ExactExpense(Expense):
    def __init__(self, amount: float, paid_by: User, splits: list[Split]):
        super(ExactExpense, self).__init__(amount, paid_by, splits)

    def validate(self):
        total_amount = 0
        for split in self.splits:
            if not isinstance(split, ExactSplit):
                return False
            total_amount = total_amount + split.get_amount()
        return total_amount == self.amount
