from entities.expense import Expense
from entities.split.percent_split import PercentSplit
from entities.split.split_entity import Split
from enums import ExpenseType
from services.expense_service.expense_service import ExpenseService


class PercentExpenseService(ExpenseService):
    def create_expense(self, paid_by_user_id: int, amount: float, splits: list[Split]) -> Expense:
        for split in splits:
            split.set_amount((amount*split.get_percent())/100)

        return Expense(paid_by_user_id, amount, ExpenseType.PERCENT_EXPENSE.value, splits)

    def validate_expense(self, paid_by_user_id: int, amount: float, splits: list[Split]) -> bool:
        total_percent = 0

        if paid_by_user_id <= 0 or amount <= 0:
            return False

        for split in splits:
            if not isinstance(split, PercentSplit):
                return False
            total_percent += split.get_percent()

        return total_percent == 100.00
