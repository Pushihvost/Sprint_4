import pytest

@pytest.fixture
def book_with_genre():
    name = "Кот Саймона"
    genre = "Комедии"
    books = BooksCollector()
    books.add_new_book(name)
    books.set_book_genre(name, genre)
    return books

@pytest.fixture
def books_full():
    books = BooksCollector()

    data = [
        ("Кот Саймона", "Комедии"),
        ("Космопсихолухи", "Комедии"),
        ("Дракула", "Ужасы"),
        ("Дюна", "Фантастика"),
    ]

    for name, genre in data:
        books.add_new_book(name)
        books.set_book_genre(name, genre)

    return books

@pytest.fixture
def book_add_in_favorite(book_with_genre):
    books = book_with_genre
    books.add_book_in_favorites("Кот Саймона")
    return books
