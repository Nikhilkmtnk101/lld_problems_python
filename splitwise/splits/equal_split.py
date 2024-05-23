from splitwise.splits.split import Split
from splitwise.user.user import User


class EqualSplit(Split):
    def __init__(self, user: User):
        super(EqualSplit, self).__init__(user)
