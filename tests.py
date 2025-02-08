from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_assign_genre_to_book(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        genre = 'Фантастика'
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre_after_setting_genre(self):
        collector = BooksCollector()
        book_name = 'Властелин колец'
        collector.add_new_book(book_name)
        genre = 'Фантастика'
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_books_exist(self):
        collector = BooksCollector()
        book1_name = 'Гарри Поттер'
        book2_name = 'Властелин колец'
        collector.add_new_book(book1_name)
        collector.add_new_book(book2_name)
        genre_fantastic = 'Фантастика'
        collector.set_book_genre(book1_name, genre_fantastic)
        collector.set_book_genre(book2_name, genre_fantastic)
        assert collector.get_books_with_specific_genre(genre_fantastic) == [book1_name, book2_name]

    def test_get_books_genre_add_two_books(self):
        collector = BooksCollector()
        book1_name = 'Гарри Поттер'
        book2_name = 'Властелин колец'
        genre_fantastic = 'Фантастика'
        genre_uzhasy = 'Ужасы'
        collector.add_new_book(book1_name)
        collector.add_new_book(book2_name)
        collector.set_book_genre(book1_name, genre_fantastic)
        collector.set_book_genre(book2_name, genre_uzhasy)
        expected_books_genre = {
            book1_name: genre_fantastic,
            book2_name: genre_uzhasy,
        }
        assert collector.get_books_genre() == expected_books_genre

    def test_get_books_for_children_without_genre_age_rating(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Аватар': 'Фантастика',
            'Астрал': 'Ужасы',
            'Остров проклятых': 'Детективы',
            'Тачки': 'Мультфильмы',
            'Пока не сыграл в ящик': 'Комедии',
            'Книга 6': 'Поэзия'  # <-- Жанр отсутствует в списке доступных жанров
        }
        expected_books = ['Аватар', 'Тачки', 'Пока не сыграл в ящик']
        assert collector.get_books_for_children() == expected_books

    def test_add_book_in_favorites_one_books_added(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Аватар': 'Фантастика',
            'Астрал': 'Ужасы',
            'Остров проклятых': 'Детективы'
        }
        collector.add_book_in_favorites('Аватар')
        assert 'Аватар' in collector.favorites
        collector.add_book_in_favorites('Аватар')
        assert collector.favorites.count('Аватар') == 1
        collector.add_book_in_favorites('Тачки')
        assert 'Тачки' not in collector.favorites

    def test_delete_book_from_favorites_one_book_delete(self):
        collector = BooksCollector()
        collector.books_genre = {'Аватар': 'Фантастика'}
        collector.favorites = ['Аватар']

        collector.delete_book_from_favorites('Аватар')
        assert 'Аватар' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.favorites = ['Аватар', 'Астрал']
        assert collector.get_list_of_favorites_books() == ['Аватар', 'Астрал']


