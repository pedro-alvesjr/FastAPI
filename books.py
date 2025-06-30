from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'genre': 'History'},
    {'title': 'Title Two', 'author': 'Author Two', 'genre': 'Fiction'},
    {'title': 'Title Three', 'author': 'Author Three', 'genre': 'Sci-fi'},
    {'title': 'Title Four', 'author': 'Author Four', 'genre': 'Fiction'},
    {'title': 'Title Five', 'author': 'Author Two', 'genre': 'History'},
]

@app.get("/books")
def show_all_books():
    return BOOKS

@app.get('/books/{book_title}')
def show_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book