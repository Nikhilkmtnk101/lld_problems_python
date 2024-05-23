from splitwise.enum import ExpenseType
from splitwise.expense.equal_expense import EqualExpense
from splitwise.expense.exact_split import ExactExpense
from splitwise.expense.percent_expense import PercentExpense
from splitwise.splits.split import Split
from splitwise.user.user import User


class ExpenseFactory:
    @staticmethod
    def create_expense(expense_type: ExpenseType, amount: float, paid_by: User, splits: list[Split]):
        expense = None
        if expense_type == ExpenseType.EQUAL_EXPENSE.value:
            splits_count = len(splits)
            split_amount = round(amount/splits_count, 2)
            for split in splits:
                split.set_amount(split_amount)
            splits[0].set_amount(split_amount+amount-splits_count*split_amount)
            expense = EqualExpense(amount, paid_by, splits)
        elif expense_type == ExpenseType.EXACT_EXPENSE.value:
            expense = ExactExpense(amount, paid_by, splits)
        elif expense_type == ExpenseType.PERCENT_EXPENSE.value:
            for split in splits:
                split_amount = (split.get_percent()*amount)/100
                split.set_amount(split_amount)
            expense = PercentExpense(amount, paid_by, splits)
        else:
            raise Exception("Invalid Expense Type")

        return expense
