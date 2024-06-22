from library_management_system.models.rack import Rack


class Library:
    def __init__(self, library_id: str, capacity: int):
        self.library_id = library_id
        self.capacity = capacity
        self.empty_rack_count = capacity
        self.racks = [Rack(i) for i in range(1, capacity + 1)]

    def get_library_id(self) -> str:
        return self.library_id

    def get_capacity(self) -> int:
        return self.capacity

    def get_racks(self) -> list[Rack]:
        return self.racks

    def get_empty_rack_count(self) -> int:
        return self.empty_rack_count

    def add_book(self, rack_id: int, book_copy_id: str):
        self.racks[rack_id-1].place_book_copy(book_copy_id)
        self.empty_rack_count -= 1

    def remove_book(self, rack_id: int):
        self.empty_rack_count += 1
        return self.racks[rack_id-1].remove_book_copy()
