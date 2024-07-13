from entities.expense import Expense
from entities.split.exact_split import ExactSplit
from entities.split.split_entity import Split
from enums import ExpenseType
from services.expense_service.expense_service import ExpenseService


class ExactExpenseService(ExpenseService):
    def create_expense(self, paid_by_user_id: int, amount: float, splits: list[Split]) -> Expense:
        return Expense(paid_by_user_id, amount, ExpenseType.EXACT_EXPENSE.value, splits)

    def validate_expense(self, paid_by_user_id: int, amount: float, splits: list[Split]) -> bool:
        total_amount = 0

        if paid_by_user_id <= 0 or amount <= 0:
            return False

        for split in splits:
            total_amount += split.get_amount()
            if not isinstance(split, ExactSplit):
                return False

        return total_amount == amount
