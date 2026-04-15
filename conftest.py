import pytest

@pytest.fixture
def book_with_genre():
    name = "Êîò Ñàéìîíà"
    genre = "Êîìåäèè"
    books = BooksCollector()
    books.add_new_book(name)
    books.set_book_genre(name, genre)
    return books

@pytest.fixture
def books_full():
    books = BooksCollector()

    data = [
        ("Êîò Ñàéìîíà", "Êîìåäèè"),
        ("Êîñìîïñèõîëóõè", "Êîìåäèè"),
        ("Äðàêóëà", "Óæàñû"),
        ("Äþíà", "Ôàíòàñòèêà"),
    ]

    for name, genre in data:
        books.add_new_book(name)
        books.set_book_genre(name, genre)

    return books

@pytest.fixture
def book_add_in_favorite():
    name = "Êîò Ñàéìîíà"
    genre = "Êîìåäèè"

    books = BooksCollector()

    books.add_new_book(name)
    books.set_book_genre(name, genre)
    books.add_book_in_favorites(name)

    return books
