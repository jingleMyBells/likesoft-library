from django.conf import settings
from django.db import models


class Book(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=settings.BOOK_PROPS.get('title_length', 255),
    )
    author = models.CharField(
        verbose_name='автор',
        max_length=settings.BOOK_PROPS.get('author_length', 255),
    )
    pub_year = models.PositiveIntegerField(
        verbose_name='год издания',
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=settings.BOOK_PROPS.get('isbn_length', 255),
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title + '; ' + self.author
