from splitwise.enums import ExpenseType
from splitwise.services.expense_service.equal_expense_service import EqualExpenseService
from splitwise.services.expense_service.exact_expense_service import ExactExpenseService
from splitwise.services.expense_service.expense_service import ExpenseService
from splitwise.services.expense_service.percent_expense_service import PercentExpenseService


class ExpenseServiceFactory:
    
    @staticmethod
    def get_expense_service(expense_type: str) -> ExpenseService:
        expense_service = None
        if expense_type == ExpenseType.EQUAL_EXPENSE.value:
            expense_service = EqualExpenseService()
        elif expense_type == ExpenseType.EXACT_EXPENSE.value:
            expense_service = ExactExpenseService()
        elif expense_type == ExpenseType.PERCENT_EXPENSE.value:
            expense_service = PercentExpenseService()

        return expense_service
