from splitwise.enum import ExpenseType
from splitwise.expense.expense_factory import ExpenseFactory
from splitwise.splits.split import Split
from splitwise.user.user import User


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.users = {}
        self.balance_sheet_map = {}

    @staticmethod
    def print_balance(user1_id: str, user2_id: str, amount: float):
        if amount > 0:
            print(f'{user2_id} owes {user1_id}: {abs(amount)}')
        elif amount < 0:
            print(f'{user1_id} owes {user2_id}: {abs(amount)}')

    def add_user(self, user_id: str, name: str, email: str, phone_number: str):
        user = User(user_id, name, email, phone_number)
        self.balance_sheet_map[user_id] = {}
        self.users[user_id] = user

    def add_expense(self, expense_type: ExpenseType, amount: float, paid_by: User, splits: list[Split]):
        paid_by_user_id = paid_by.user_id
        expense = ExpenseFactory.create_expense(expense_type, amount, paid_by, splits)
        if not expense.validate():
            raise Exception("Expense Validation Failed")

        self.expenses.append(expense)
        for split in expense.splits:
            paid_to_user_id = split.user.user_id
            split_amount = split.get_amount()

            paid_by_user_balance_sheet = self.balance_sheet_map.get(paid_by_user_id, {})
            if not paid_by_user_balance_sheet.get(paid_to_user_id, None):
                paid_by_user_balance_sheet[paid_to_user_id] = 0.0

            paid_by_user_balance_sheet[paid_to_user_id] = paid_by_user_balance_sheet[paid_to_user_id] + split_amount

            paid_to_user_balance_sheet = self.balance_sheet_map.get(paid_to_user_id, {})

            if not paid_to_user_balance_sheet.get(paid_by_user_id, None):
                paid_to_user_balance_sheet[paid_by_user_id] = 0.0

            paid_to_user_balance_sheet[paid_by_user_id] = paid_to_user_balance_sheet[paid_by_user_id] - split_amount

    def show_balance(self, user_id: str):
        is_empty = True

        for key, value in self.balance_sheet_map.get(user_id, {}).items():
            if value != 0.0:
                self.print_balance(user_id, key, value)
                is_empty = False

        if is_empty:
            print('No balances')
        print()

    def show_balances(self):
        is_empty = True

        for from_user_id, from_user_balance_sheet in self.balance_sheet_map.items():
            for to_user_id, amount in from_user_balance_sheet.items():
                if amount > 0.0:
                    self.print_balance(from_user_id, to_user_id, amount)
                    is_empty = False

        if is_empty:
            print('No balances')

        print()



