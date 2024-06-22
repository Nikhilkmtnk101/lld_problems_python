
class BookCopy:
    def __init__(self, book_copy_id: str, book_id: str):
        self.book_copy_id = book_copy_id
        self.book_id = book_id

    def get_book_copy_id(self) -> str:
        return self.book_copy_id

    def get_book_id(self) -> str:
        return self.book_id
