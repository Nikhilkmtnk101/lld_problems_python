from splitwise.entities.split.split_entity import Split


class ExactSplit(Split):
    def __init__(self, user_id, amount=0.0):
        super().__init__(user_id, amount)
