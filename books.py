from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'History'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'Fiction'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'Sci-fi'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'Fiction'},
    {'title': 'Title Five', 'author': 'Author Two', 'category': 'History'},
]

@app.get("/books")
def show_all_books():
    return BOOKS

@app.get('/books/{book_title}')
def show_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get('/books/')
def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return