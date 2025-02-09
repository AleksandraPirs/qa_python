# qa_python
1. В первом тесте для функции add_new_book добавили две книги для проверки и проверили, что кол-во добавляемых книг совпадает
2. Во втором тесте для функции set_book_genre добавили книгу и установили ей жанр, потом проверили что жанр установлен для книги корректно
3. В третьем тесте для функции set_book_genre добавили книгу и установили ей несуществующий жанр, проверили, что жанр книги не изменился
4. В четвертом тесте для функции get_book_genre проверяем, что для книги с установленным жанром возвращается правильный жанр
5. В пятом тесте для функции get_book_genre проверяем, что для книги без установленного жанра возвращается None
6. В шестом тесте для функции get_book_genre проверяем, что для несуществующей книги возвращается None
7. В седьмом тесте для функции get_books_with_specific_genre проверяет, что для жанра, книги которого присутствуют в коллекции, возвращается правильный список книг.
8. В восьмом тесте для функции get_books_with_specific_genre проверяет, что для жанра, книги которого отсутствуют, возвращается пустой список.
9. В девятом тесте для функции get_books_with_specific_genre проверяет, что для несуществующего в genre жанра, возвращается пустой список.
10. В десятом тесте для функции get_books_genre проверяет, что метод get_books_genre возвращает точный словарь books_genre, который ожидается.  
11. В одиннадцатом тесте для функции get_books_for_children, проверяет, что функция get_books_for_children возвращает правильный список книг, которые не содержат жанры с возрастными ограничениями.
12. В двенадцатом тесте для функции add_book_in_favorites, проверяет, что книга добавляется в список избранных только если она существует в коллекции.
13. В тринадцатом тесте для функции add_book_in_favorites, проверяет, что нет дублирующих записей для одной и той же книги в списке избранных. 
14. В четырнадцатом тесте для функции delete_book_from_favorites проверяем, что книга удалена из списка избранных
15. В пятнадцатом тесте для функции delete_book_from_favorites пробуем удалить книгу, которой нет в избранном и убеждаемся, что список избранных остался без изменений
16. В шестнадцатом тесте для функции get_list_of_favorites_books проверяем, что полученный список избранных книг соотвествует ожиданию.


