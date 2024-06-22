class Rack:
    def __init__(self, rack_id: int):
        self.rack_id = rack_id
        self.is_empty = True
        self.book_copy_id = None

    def get_rack_id(self) -> int:
        return self.rack_id

    def is_rack_empty(self):
        return self.is_empty

    def get_placed_book_copy_id(self) -> str:
        return self.book_copy_id

    def place_book_copy(self, book_copy_id: str):
        self.is_empty = False
        self.book_copy_id = book_copy_id

    def remove_book_copy(self) -> str:
        self.is_empty = True
        removed_book_copy_id = self.book_copy_id
        self.book_copy_id = None
        return removed_book_copy_id
