from flask import Flask, request
from book import Book, BookList

app = Flask(__name__)

books = BookList(Book("John Johnson", "Book Title"), Book("Dorothy", "The wonderful world of os"))
books.update_ids()


def get_args():
    return {key: value for key, value in request.args.items() if key in ("title", "author")}


@app.route('/')
def index():
    return [book.json for book in books.filter(**get_args())]


@app.route('/create')
def create():
    try:
        book = books.create(**get_args())
        return book.json

    except TypeError as err:
        return str(err)


@app.route('/<int:book_id>')
def get(book_id):
    return books.get(book_id).json


@app.route('/<int:book_id>/delete')
def delete(book_id):
    books.delete(book_id)
    return ""


@app.route('/<int:book_id>/update')
def update(book_id):
    return books.update(book_id, **get_args()).json


if __name__ == "__main__":
    app.run(debug=True)