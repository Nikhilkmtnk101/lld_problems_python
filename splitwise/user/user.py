class User:
    def __init__(self, user_id: str, name: str, email: str, phone_number: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_email(self, email: str):
        self.email = email

    def get_email(self) -> str:
        return self.email

    def set_phone(self, phone_number: str):
        self.phone_number = phone_number

    def get_phone_number(self) -> str:
        return self.phone_number

