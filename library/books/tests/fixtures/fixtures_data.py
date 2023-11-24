import pytest

from books.models import Book


@pytest.fixture
def book_1():
    return Book.objects.create(
        title='Звезда Пандоры',
        author='Питер Гамильтон',
        pub_year=2004,
        isbn='978-5-91878-585-0'
    )


@pytest.fixture
def book_2():
    return Book.objects.create(
        title='Должность во вселенной',
        author='Владимир Савченко',
        pub_year=1992,
        isbn='978-5-389-15504-6'
    )
