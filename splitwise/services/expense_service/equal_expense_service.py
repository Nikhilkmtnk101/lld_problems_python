from entities.expense import Expense
from entities.split.equal_split import EqualSplit
from entities.split.split_entity import Split
from enums import ExpenseType
from services.expense_service.expense_service import ExpenseService


class EqualExpenseService(ExpenseService):
    def create_expense(self, paid_by_user_id: int, amount: float, splits: list[Split]) -> Expense:
        no_of_users = len(splits)
        split_amount = round(amount/no_of_users, 2)
        for split in splits:
            split.set_amount(split_amount)

        return Expense(paid_by_user_id, amount, ExpenseType.EQUAL_EXPENSE.value, splits)

    def validate_expense(self, paid_by_user_id: int, amount: float, splits: list[Split]) -> bool:
        if paid_by_user_id <= 0 or amount <= 0:
            return False

        for split in splits:
            if not isinstance(split, EqualSplit):
                return False

        return True
