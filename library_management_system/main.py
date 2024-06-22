from library_management_system.library_manager import LibraryManager
from library_management_system.service.user_service import UserService

if __name__ == '__main__':
    library_manger = LibraryManager()
    library_manger.create_library("lib1", 10)

    user_service = UserService()
    user_service.create_user("user1", "Nikhil1", 5)

    library_manger.add_book(
        "1",
        "book1",
        ["author1", "author2"],
        ["publisher1"],
        ["book_copy1", "book_copy2", "book_copy3"]
    )

    library_manger.add_book(
        "2",
        "book2",
        ["author2", "author3"],
        ["publisher2", "publisher3"],
        ["book_copy4", "book_copy5", "book_copy6", "book_copy7", "book_copy8", "book_copy9", "book_copy10"]
    )