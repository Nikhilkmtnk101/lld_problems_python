from splitwise.user.user import User


class UserBalanceSheet:
    def __init__(self, owner: User):
        self.owner = owner
        self.balance_sheet = {}

    def get_owner(self) -> User:
        return self.user

    def set_owner(self, owner: User):
        self.owner = owner

    def get_balance_sheet(self) -> dict:
        return self.balance_sheet

    def set_balance_sheet(self, balance_sheet: dict):
        self.balance_sheet = balance_sheet
