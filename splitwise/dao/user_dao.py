class UserDao:
    def __init__(self):
        self.users = {}

    def get_users(self):
        return self.users

    def set_users(self, users):
        self.users = users

    def save_user(self, user):
        self.users[user.get_user_id()] = user

    def get_user_by_id(self, user_id):
        return self.users.get(user_id, None)

