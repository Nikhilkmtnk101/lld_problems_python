from splitwise.dao.user_dao import UserDao
from splitwise.entities.split.split_entity import Split
from splitwise.entities.user import User
from splitwise.services.balance_sheet_manager import BalanceSheetService
from splitwise.services.expense_service.expense_service_factory import ExpenseServiceFactory


class SplitWise:
    def __init__(self):
        self.user_dao = UserDao()
        self.balance_sheet_service = BalanceSheetService()
        self.expense_service_factory = ExpenseServiceFactory()

    "Public Methods"

    def create_user(self, name: str, phone: str, email: str) -> int:
        user = User(name, phone, email)
        self.user_dao.save_user(user)
        return user.get_user_id()

    def create_expense(self, paid_by_user_id: int, amount: float, expense_type: str, splits: list[Split]):
        expense_service = self.expense_service_factory.get_expense_service(expense_type)

        is_valid_request = expense_service.validate_expense(paid_by_user_id, amount, splits)
        if not is_valid_request:
            print(f" Given request is not valid")
            return

        expense = expense_service.create_expense(paid_by_user_id, amount, splits)
        self.balance_sheet_service.update_balances(expense)

    def get_balance_by_user_id(self, user_id):
        self.balance_sheet_service.show_balance_by_user_id(user_id)
        print()

    def get_balance(self):
        self.balance_sheet_service.show_balances()
        print()
