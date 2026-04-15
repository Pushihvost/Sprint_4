from main import BooksCollector
import pytest

class TestBooksCollector():
    
    def test_init_sets_default_values():
        books = BooksCollector()

        assert books.books_genre == {}
        assert books.favorites == []
        assert books.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books.genre_age_rating == ['Ужасы', 'Детективы']
    
    @pytest.mark.parametrize('name', ['', 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfg'])
    def test_add_new_book_invalid_name_length(self, name): 
        books = BooksCollector()
        books.add_new_book(name)
        assert books.books_genre == {}

    def test_set_book_genre_sets_correct_genre(self, book_with_genre):

        assert book_with_genre.books_genre == {"Кот Саймона": "Комедии"}

    def test_get_book_genre_returns_correct_genre(self, book_with_genre):
        
        assert book_with_genre.get_book_genre("Кот Саймона") == "Комедии"

    def test_get_books_with_specific_genre_returns_two_comedy_books(self, books_full):       

        assert books_full.get_books_with_specific_genre("Комедии") == ["Кот Саймона", "Космопсихолухи"]

    def test_get_books_genre_returns_correct_dictionary(self, book_with_genre):

        assert book_with_genre.get_books_genre() == {"Кот Саймона":"Комедии"}                                                     

    def test_get_books_for_children_excludes_age_restricted_genres(self, books_full):

        assert books_full.get_books_for_children() == ["Кот Саймона","Космопсихолухи", "Дюна"]

    def test_add_book_in_favorites_adds_book(self, book_add_in_favorite):

        assert book_add_in_favorite.favorites == ["Кот Саймона"]

    def test_add_book_in_favorites_no_duplicates(self, book_add_in_favorite):

        book_add_in_favorite.add_book_in_favorites("Кот Саймона")

        assert book_add_in_favorite.favorites == ["Кот Саймона"]

    def test_delete_book_from_favorites_removes_book(self, book_add_in_favorite):

        book_add_in_favorite.delete_book_from_favorites("Кот Саймона")

        assert book_add_in_favorite.favorites == []

    def test_get_list_of_favorites_books_returns_list(self, book_add_in_favorite):

        assert book_add_in_favorite.get_list_of_favorites_books() == ["Кот Саймона"]
