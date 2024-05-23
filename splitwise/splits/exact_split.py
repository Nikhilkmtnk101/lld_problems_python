from splitwise.splits.split import Split
from splitwise.user.user import User


class ExactSplit(Split):
    def __init__(self, user: User, amount: float):
        super(ExactSplit, self).__init__(user)
        super(ExactSplit, self).set_amount(amount)


