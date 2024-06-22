class Book:
    def __init__(self, book_id: str, title: str, authors: list[str], publishers: list[str]):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.publishers = publishers

    def get_book_id(self) -> str:
        return self.book_id

    def get_title(self) -> str:
        return self.title

    def get_authors(self) -> list[str]:
        return self.authors

    def get_publishers(self) -> list[str]:
        return self.authors




