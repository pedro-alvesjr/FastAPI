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