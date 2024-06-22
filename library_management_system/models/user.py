class User:
    def __init__(self, user_id: str, name: str, maximum_count: int):
        self.user_id = user_id
        self.name = name
        self.maximum_count = maximum_count
        self.borrowed_books = []

    def get_user_id(self) -> str:
        return self.user_id

    def get_name(self) -> str:
        return self.name

    def get_maximum_count(self) -> int:
        return self.maximum_count

    def set_maximum_count(self, maximum_count: int):
        self.maximum_count = maximum_count

    def get_borrowed_books(self) -> list[list[str]]:
        return self.borrowed_books

    def can_borrow_book(self) -> bool:
        return self.maximum_count > len(self.borrowed_books)

    def add_book_id(self, book_copy_id: str, due_date: str):
        self.borrowed_books.append([book_copy_id, due_date])


