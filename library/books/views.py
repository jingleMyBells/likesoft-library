from rest_framework import viewsets

from books.models import Book
from books.serializers import BookCreateSerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    #FIXME! Добавить пагинацию
    #FIXME! Если будет время, добавить фильтр для поиска

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'create':
            return BookCreateSerializer
        return BookSerializer
