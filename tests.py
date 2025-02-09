import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture
    def collector_with_books(self):
        collector = BooksCollector()
        # Добавляем книги в коллекцию
        collector.books_genre = {
            'Аватар': 'Фантастика',
            'Остров проклятых': 'Детективы',
            'Шрек': 'Мультфильмы',
            'Клаустрофобы': 'Ужасы',
            'Штрафной бросок': 'Детективы'
        }
        return collector

    def test_add_new_book_add_two_books(self): #проверили добавление новых книг
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_correctly(self, collector_with_books): #проверяем установку жанра книге
        # Назначаем жанр книге
        book_name = 'Аватар'
        genre = 'Фантастика'
        collector_with_books.set_book_genre(book_name, genre)
        # Проверяем, что жанр книги правильно установлен
        assert collector_with_books.books_genre[book_name] == genre

    def test_set_book_genre_invalid_genre(self, collector_with_books): #проверяем, что несуществующий жанр не устанавливается
        # Пытаемся установить несуществующий жанр
        book_name = 'Аватар'
        invalid_genre = 'Боевик'
        # Перед установкой проверяем, что жанр еще не установлен
        original_genre = collector_with_books.books_genre[book_name]
        collector_with_books.set_book_genre(book_name, invalid_genre)
        # Проверяем, что жанр книги не изменился
        assert collector_with_books.books_genre[book_name] == original_genre

    def test_get_book_genre_existing_book_with_genre(self, collector_with_books):
        # Проверяем, что для книги с установленным жанром возвращается правильный жанр
        book_name = 'Аватар'
        expected_genre = 'Фантастика'
        result = collector_with_books.get_book_genre(book_name)
        assert result == expected_genre

    def test_get_book_genre_existing_book_without_genre(self, collector_with_books):
        # Проверяем, что для книги без установленного жанра возвращается None
        book_name = 'Гордость и предубеждение и зомби'
        expected_genre = None
        result = collector_with_books.get_book_genre(book_name)
        assert result == expected_genre

    def test_get_book_genre_non_existing_book(self, collector_with_books):
        # Проверяем, что для несуществующей книги возвращается None
        book_name = 'Игры разума'
        expected_genre = None
        result = collector_with_books.get_book_genre(book_name)
        assert result == expected_genre

    def test_get_books_with_specific_genre_existing_genre(self, collector_with_books):
        #Проверяет, что для жанра, книги которого присутствуют в коллекции, возвращается правильный список книг
        genre = 'Детективы'
        expected_books = ['Остров проклятых', 'Штрафной бросок']
        result = collector_with_books.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_with_specific_genre_no_books_for_genre(self, collector_with_books):
        #Проверяет, что для жанра, книги которого отсутствуют, возвращается пустой список.
        genre = 'Комедии'
        expected_books = []
        result = collector_with_books.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_with_specific_genre_non_existing_genre(self, collector_with_books):
        #Проверяет, что для несуществующего в genre жанра, возвращается пустой список.
        genre = 'Романтика'
        expected_books = []
        result = collector_with_books.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_genre_return_books_genre(self, collector_with_books):
        #Проверяет, что метод get_books_genre возвращает точный словарь books_genre, который ожидается.
        expected_books_genre = {
            'Аватар': 'Фантастика',
            'Остров проклятых': 'Детективы',
            'Шрек': 'Мультфильмы',
            'Клаустрофобы': 'Ужасы',
            'Штрафной бросок': 'Детективы'
        }
        result = collector_with_books.get_books_genre()
        assert result == expected_books_genre

    def test_get_books_for_children_two_books(self, collector_with_books):
    # Ожидаем, что только книги без ограничений по возрасту будут в списке
        expected_books_for_children = ['Аватар', 'Шрек']
        result = collector_with_books.get_books_for_children()
        assert result == expected_books_for_children

    def test_add_book_in_favorites_book_to_add(self, collector_with_books):
        # Добавляем книгу в избранное
        book_to_add = 'Аватар'
        collector_with_books.add_book_in_favorites(book_to_add)
        # Проверяем, что книга добавилась в список избранных
        assert book_to_add in collector_with_books.favorites

    def test_add_book_in_favorites_book_twice_to_add(self, collector_with_books):
        book_to_add = 'Аватар'
        # Пробуем добавить ту же книгу снова
        collector_with_books.add_book_in_favorites(book_to_add)
        # Убедимся, что в избранных нет дублирующих записей
        assert collector_with_books.favorites.count(book_to_add) == 1

    def test_delete_book_from_favorites(self, collector_with_books):
        book_to_add = 'Аватар'
        collector_with_books.add_book_in_favorites(book_to_add)
        book_to_remove = 'Аватар'
        collector_with_books.delete_book_from_favorites(book_to_remove)
        # Проверяем, что книга удалена из списка избранных
        assert book_to_remove not in collector_with_books.favorites

    def test_delete_book_from_favorites_no_book(self, collector_with_books):
        # Пробуем удалить книгу, которой нет в избранном
        book_to_add = 'Аватар'
        collector_with_books.add_book_in_favorites(book_to_add)
        book_to_remove = 'Остров проклятых'
        collector_with_books.delete_book_from_favorites(book_to_remove)
        # Убеждаемся, что список избранных остался без изменений
        assert collector_with_books.favorites == ['Аватар']

    def test_get_list_of_favorites_books(self, collector_with_books):
        collector_with_books.favorites = ['Аватар', 'Остров проклятых']
        # Получаем список избранных книг
        favorites = collector_with_books.get_list_of_favorites_books()
        # Проверяем, что список избранных соответствует ожиданиям
        assert favorites == ['Аватар', 'Остров проклятых']