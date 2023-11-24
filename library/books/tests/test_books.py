import pytest

from books.models import Book


class TestBooksAPI:

    def setup_class(self):
        self.url_books = '/api/v1/books/'

    @pytest.mark.django_db(transaction=True)
    def test_books_not_auth(self, client):
        response = client.get(self.url_books)

        assert response.status_code == 200, (
            'Апи отвечает некорректным статусом '
            'при запросе книг неавторизованным пользователем',
        )

    @pytest.mark.django_db(transaction=True)
    def test_books_correct_data(self, client, book_1, book_2):
        response = client.get(self.url_books)
        books = response.json()

        assert isinstance(books, list), (
            'Получение книг не результирует в список',
        )
        assert len(books) == 2, (
            'Количество книг не соответствует фикстуре',
        )

        title = books[0]['title']

        assert title == book_1.title, (
            'Название первой книги не совпадает с ожидаемым',
        )

    @pytest.mark.django_db(transaction=True)
    def test_book_fields(self, client, book_1):
        response = client.get(self.url_books)

        books = response.json()
        test_book = books[0]
        for field in Book._meta.fields:
            assert field.name in test_book, (
                f'Нет поля {field.name} в ответе {self.url_books}'
            )

    @pytest.mark.django_db(transaction=True)
    def test_invalid_book_title(self, client):
        data = {
            'title': 'Название для умножения'*100,
            'author': 'Вполне валидный автор',
            'pub_year': 2022,
            'isbn': 'В-а-л-и-д-н-о-т-а'
        }

        response = client.post(self.url_books, data=data)

        assert response.status_code == 400, (
            'Вернулся не 400 статус при невалидном названии книги',
        )

    @pytest.mark.django_db(transaction=True)
    def test_invalid_book_author(self, client):
        data = {
            'title': 'Вполне валидное название',
            'author': 'Вася'*100,
            'pub_year': 2022,
            'isbn': 'В-а-л-и-д-н-о-т-а',
        }

        response = client.post(self.url_books, data=data)

        assert response.status_code == 400, (
            'Вернулся не 400 статус при невалидном авторе книги',
        )

    @pytest.mark.django_db(transaction=True)
    def test_invalid_book_pub_year(self, client):
        data = {
            'title': 'Вполне валидное название',
            'author': 'Вполне валидный автор',
            'pub_year': 2030,
            'isbn': 'В-а-л-и-д-н-о-т-а',
        }

        response = client.post(self.url_books, data=data)

        assert response.status_code == 400, (
            'Вернулся не 400 статус при невалидном годе публикации книги',
        )

        data = {
            'title': 'Вполне валидное название',
            'author': 'Вполне валидный автор',
            'pub_year': 10,
            'isbn': 'В-а-л-и-д-н-о-т-а',
        }

        response = client.post(self.url_books, data=data)

        assert response.status_code == 400, (
            'Вернулся не 400 статус при невалидном годе публикации книги',
        )

    @pytest.mark.django_db(transaction=True)
    def test_invalid_book_isbn(self, client):
        data = {
            'title': 'Вполне валидное название',
            'author': 'Вполне валидный автор',
            'pub_year': 2022,
            'isbn': 'lalala'*100,
        }

        response = client.post(self.url_books, data=data)

        assert response.status_code == 400, (
            'Вернулся не 400 статус при невалидном ISBN книги',
        )

    @pytest.mark.django_db(transaction=True)
    def test_category_non_exist(self, client, book_1, book_2):
        response = client.get(self.url_books + '3/')

        assert response.status_code == 404, (
            'Не возвращается 404 ошибка при несуществующем объекте',
        )
