from splitwise.user.user import User


class Split:
    def __init__(self, user: User):
        self.user = user
        self.amount = 0

    def set_user(self, user: User):
        self.user = user

    def get_user(self) -> User:
        return self.user

    def set_amount(self, amount: float):
        self.amount = amount

    def get_amount(self) -> float:
        return self.amount

