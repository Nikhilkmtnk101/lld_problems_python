from library_management_system.models.user import User


class UserService:
    def __init__(self):
        self.user_id_vs_users = {}

    def create_user(self, user_id: str, name: str, maximum_count: int):
        self.user_id_vs_users[user_id] = User(user_id, name, maximum_count)

    def get_user_by_id(self, user_id: str) -> User:
        return self.user_id_vs_users.get(user_id, None)