from splitwise.entities.expense import Expense


class BalanceSheetService:
    def __init__(self):
        self.balances = {}

    "Private Methods"
    def __add_balance(self, from_account_id, to_account_id, amount):
        current_amount = self.balances.get(from_account_id, {}).get(to_account_id, 0)
        if not self.balances.get(from_account_id, None):
            self.balances[from_account_id] = {}
        self.balances[from_account_id][to_account_id] = current_amount + amount

    @staticmethod
    def __display_balance_sheet(from_account_id: int, to_account_id: int, amount: float):
        if amount > 0.0:
            print(f'User{to_account_id} owes User{from_account_id}: {amount}')
        elif amount < 0.0:
            print(f'User{from_account_id} owes User{to_account_id}: {abs(amount)}')

    "Public Methods"
    def update_balances(self, expense: Expense):
        expense_paid_by = expense.get_paid_by()

        for split in expense.get_splits():
            expense_paid_to = split.get_users_id()
            split_amount = split.get_amount()
            self.__add_balance(expense_paid_by, expense_paid_to, split_amount)
            self.__add_balance(expense_paid_to, expense_paid_by, -split_amount)

    def show_balance_by_user_id(self, user_id: int):
        user_balance_sheet = self.balances.get(user_id, {})

        if len(user_balance_sheet) == 0:
            print("NO BALANCE")
            return

        for to_user_id, amount in user_balance_sheet.items():
            self.__display_balance_sheet(user_id, to_user_id, amount)

    def show_balances(self):

        if len(self.balances) == 0:
            print("NO BALANCE")
            return

        for user_id, user_balance_sheet in self.balances.items():
            for to_user_id, amount in user_balance_sheet.items():
                self.__display_balance_sheet(user_id, to_user_id, amount)


