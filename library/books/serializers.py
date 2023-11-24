from datetime import datetime as dt

from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

import books.constants as const
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=settings.BOOK_PROPS.get('title_length', 255),
        required=True,
    )
    author = serializers.CharField(
        max_length=settings.BOOK_PROPS.get('author_length', 255),
        required=True,
    )
    pub_year = serializers.IntegerField(required=True)
    isbn = serializers.CharField(
        max_length=settings.BOOK_PROPS.get('isbn_length', 255),
        required=True,
    )

    class Meta:
        model = Book
        exclude = ('id',)

    def validate_pub_year(self, value):
        if value < const.FIRST_PUB_YEAR:
            raise ValidationError(const.PUB_YEAR_BEFORE_704)
        if value > dt.now().year:
            raise ValidationError(const.PUB_YEAR_AFTER_CURRENT_YEAR)
        return value
