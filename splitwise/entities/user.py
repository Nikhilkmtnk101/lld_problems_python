from splitwise.utils.user_id_generator import UserIdGenerator


class User:
    def __init__(self, name, phone, email):
        self.user_id = UserIdGenerator.get_next_user_id()
        self.name = name
        self.phone = phone
        self.email = email

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone =phone

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
