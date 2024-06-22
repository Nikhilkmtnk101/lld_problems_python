from library_management_system.models.book_copy import BookCopy


class BookCopyService:
    def __init__(self):
        self.book_copy_id_vs_book_copy = {}
        self.book_id_vs_book_copy_id = {}

    def create_book_copy(self, book_copy_id: str, book_id: str):
        self.book_copy_id_vs_book_copy[book_copy_id] = BookCopy(book_copy_id, book_id)

        if not self.book_id_vs_book_copy_id.get(book_id, None):
            self.book_id_vs_book_copy_id[book_id] = []

        self.book_id_vs_book_copy_id[book_id].append(book_copy_id)

    def search_book_by_book_copy_id(self, book_copy_id: str):
        return self.book_copy_id_vs_book_copy.get(book_copy_id, None)

    def get_book_copy_ids_by_book_id(self, book_id: str):
        return self.book_id_vs_book_copy_id.get(book_id, None)


