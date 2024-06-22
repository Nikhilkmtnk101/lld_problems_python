from library_management_system.models.book import Book


class BookService:
    def __init__(self):
        self.book_id_vs_book = {}
        self.title_vs_book_id = {}
        self.author_vs_book_id = {}
        self.publisher_vs_book_id = {}

    def create_book(self, book_id: str, title: str, authors: list[str], publishers: list[str]):
        book = Book(book_id, title, authors, publishers)
        self.book_id_vs_book[book_id] = book
        self.title_vs_book_id[title] = book_id
        for author in authors:
            if not self.author_vs_book_id.get(author, None):
                self.author_vs_book_id[author] = []
            self.author_vs_book_id[author].append(book_id)

        for publisher in publishers:
            if not self.publisher_vs_book_id.get(publisher, None):
                self.publisher_vs_book_id[publisher] = []
            self.publisher_vs_book_id[publisher].append(book_id)

    def get_book_by_book_id(self, book_id) -> Book:
        return self.book_id_vs_book.get(book_id, None)

    def get_book_by_book_ids(self, book_ids: list[str]) -> list[Book]:
        books = []
        for book_id in book_ids:
            books.append(self.book_id_vs_book[book_id])

        return books

    def search_book_by_title(self, title: str) -> list[Book]:
        book_ids = self.title_vs_book_id.get(title, None)
        return self.get_book_by_book_ids(book_ids)

    def search_book_by_author(self, author: str) -> list[Book]:
        book_ids = self.author_vs_book_id.get(author, None)
        return self.get_book_by_book_ids(book_ids)

    def search_book_by_publisher(self, publisher: str) -> list[Book]:
        book_ids = self.publisher_vs_book_id.get(publisher, None)
        return self.get_book_by_book_ids(book_ids)
