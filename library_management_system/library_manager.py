from library_management_system.models.library import Library
from library_management_system.service.book_copy_service import BookCopyService
from library_management_system.service.book_service import BookService
from library_management_system.service.user_service import UserService


class LibraryManager:
    def __init__(self):
        self.book_service = None
        self.book_copy_service = None
        self.library = None
        self.user_service = None

    def create_library(self, library_id: str, capacity: int):
        self.library = Library(library_id, capacity)
        self.book_service = BookService()
        self.book_copy_service = BookCopyService()
        self.user_service = UserService()
        print(f"Created library with {capacity} racks\n")

    def add_book(self, book_id: str, title: str, authors: list[str], publishers: list[str], book_copy_ids: list[str]):
        empty_rack_count = self.library.get_empty_rack_count()

        if empty_rack_count < len(book_copy_ids):
            print("Rack not available")
            return

        self.book_service.create_book(book_id, title, authors, publishers)

        rack_ids = []
        book_copy_ids_idx = 0
        for rack in self.library.get_racks():
            if rack.is_rack_empty():
                self.book_copy_service.create_book_copy(book_copy_ids[book_copy_ids_idx], book_id)
                rack_ids.append(rack.rack_id)
                book_copy_ids_idx += 1

        res ='Added Book to racks: '
        for rack_id in rack_ids:
            res += str(rack_id) + " "
        print(res, "\n")

    def remove_book_copy(self, book_copy_id: str):
        rack_id = None
        for rack in self.library.get_racks():
            if not rack.is_rack_empty() and rack.get_placed_book_copy_id() and \
                    rack.get_placed_book_copy_id() == book_copy_id:
                rack_id = rack.get_rack_id()

        if rack_id:
            print(f"Removed book copy: {book_copy_id} from rack: {rack_id}")
        else:
            print(f"Invalid Book Copy ID")

    def borrow_book_by_book_id(self, book_id: str, user_id: str, due_date: str):
        user = self.user_service.get_user_by_id(user_id)

        if self.book_service.get_book_by_book_id(book_id):
            print("Invalid Book ID")
            return

        if not user.can_borrow_book():
            print("Overlimit")
            return

        rack_id = None
        book_copy_ids = self.book_copy_service.get_book_copy_ids_by_book_id(book_id)
        for rack in self.library.get_racks():
            if (not rack.is_rack_empty()) and (rack.get_placed_book_copy_id() in book_copy_ids):
                user.add_book_id(rack.get_placed_book_copy_id(), rack.get_rack_id())
                rack.remove_book_copy(rack.get_placed_book_copy_id())
                rack_id = rack.get_rack_id()
                break
        if rack_id:
            print(f'Borrowed Book from rack: {rack_id}')
        else:
            print('Not available')

    def borrow_book_copy(self, book_copy_id: str, user_id: str, due_date:str):
        user = self.user_service.get_user_by_id(user_id)
        book_copy = self.book_copy_service.search_book_by_book_copy_id(book_copy_id)
        rack_id = None

        if not book_copy:
            print("Invalid Book Copy ID")
            return

        if not user.can_borrow_book():
            print("Overlimit")
            return

        for rack in self.library.get_racks():
            if not rack.is_rack_empty() and book_copy_id == rack.get_placed_book_copy_id():
                user.add_book_id(rack.get_placed_book_copy_id(), rack.get_rack_id())
                rack.remove_book_copy(book_copy_id)
                rack_id = rack.get_rack_id()
                break

        print(f'Borrowed Book Copy from rack: {rack_id}')

    def return_book_copy(self, book_copy_id: str):
        book_copy = self.book_copy_service.search_book_by_book_copy_id(book_copy_id)

        if not book_copy:
            print("Invalid Book Copy ID")
            return

        rack_id = None
        for rack in self.library.get_racks():
            if rack.is_rack_empty():
                rack.place_book_copy(book_copy_id)
                rack_id = rack.get_rack_id()
                break

        if rack_id:
            print(f'Returned book copy {book_copy_id} and added to rack: {rack_id}')