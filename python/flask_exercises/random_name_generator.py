from flask import Flask
from random import choice

app = Flask(__name__)


# I got the initial task finished quite quickly...


first_names = [
    "David",
    "Sam",
    "Sophie",
    "Tyler",
    "Bob",
    "Jill",
    "Luke",
    "Ed",
    "Sarah",
    "William",
    "Charles"
]

last_names = [
    "Wilson",
    "Johnson",
    "Freeman",
    "Williams",
    "Foreman",
    "Smith",
    "Cook",
    "Wick"
]


class HtmlItem:
    def __init__(self, type_, text, children = None):
        self.type = type_
        self.text = text
        self._next = None
        self.children = children or []

    def __str__(self):
        return f"<{self.type}>{self.text}{''.join(child for child in self.children)}</{self.type}>{self.next or ''}"

    def __add__(self, other):
        self.next = other
        return self

    def __call__(self, environ, start_fn):
        start_fn('200 OK', [('Content-Type', 'html')])
        yield str(self)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        if self._next:
            self._next.next = value
        else:
            self._next = value



def html(type_):
    def get_item(text):
        return HtmlItem(type_, text)

    return get_item


h1 = html("h1")
h2 = html("h2")


@app.route('/')
def hello():
    first_name = choice(first_names)
    last_name = choice(last_names)

    return h1('Your chosen name is:') + h2(f"{first_name} {last_name}")


if __name__ == "__main__":
    app.run(debug=True)