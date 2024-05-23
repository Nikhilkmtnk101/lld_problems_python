from splitwise.splits.split import Split
from splitwise.user.user import User


class PercentSplit(Split):
    def __init__(self, user: User, percent: float):
        super(PercentSplit, self).__init__(user)
        self.percent = percent

    def set_percent(self, percent: float):
        self.percent = percent

    def get_percent(self) -> float:
        return self.percent
