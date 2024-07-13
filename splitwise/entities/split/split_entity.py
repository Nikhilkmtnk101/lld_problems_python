class Split:
    def __init__(self, user_id, amount=0.0):
        self.user_id = user_id
        self.amount = amount

    def get_users_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount
