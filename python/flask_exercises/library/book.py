from typing import List


class Book:
    def __init__(self, author, title, pages, isbn):
        self.id = None
        self.author = author
        self.title = title
        self.pages = pages
        self.isbn = isbn

    @property
    def json(self):
        return dict(
            _id=self.id,
            author=self.author,
            title=self.title,
            pages=self.pages,
            isbn=self.isbn
        )

    @classmethod
    def from_csv(cls, line):
        return cls(*line.split(','))

    @property
    def csv(self):
        return f"{self.author},{self.title}"


class BookList:
    def __init__(self, *args):
        self._books = list(args)

    def get(self, book_id) -> Book:
        return self.filter(id=book_id)[0]

    def delete(self, book_id) -> None:
        self._books.pop(book_id - 1)
        self.update_ids()

    def update(self, book_id, **kwargs) -> Book:
        book = self.get(book_id)

        for key, value in kwargs.items():
            setattr(book, key, value)

        return book

    def update_ids(self) -> None:
        for no, book in enumerate(self._books):
            book.id = no + 1

    def create(self, *args, **kwargs) -> Book:
        book = Book(*args, **kwargs)
        self._books.append(book)
        self.update_ids()
        return book

    def filter(self, **kwargs) -> List[Book]:
        valid = list(self._books)

        for key, value in kwargs.items():
            valid = [book for book in valid if getattr(book, key) == value]

        return valid
