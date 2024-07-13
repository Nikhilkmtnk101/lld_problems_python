class UserIdGenerator:
    user_id = 0

    @classmethod
    def get_next_user_id(cls):
        cls.user_id += 1
        return cls.user_id
