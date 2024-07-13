from splitwise.entities.split.split_entity import Split


class PercentSplit(Split):
    def __init__(self, user_id, percent=0.0, amount=0.0):
        super().__init__(user_id, amount)
        self.percent = percent

    def get_percent(self):
        return self.percent

    def set_percent(self, percent):
        self.percent = percent
