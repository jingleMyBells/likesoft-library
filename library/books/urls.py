from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books.views import BookViewSet


router_books_v1 = DefaultRouter()

router_books_v1.register(
    r'books',
    BookViewSet,
    basename='books'
)

urlpatterns = [
    path('', include(router_books_v1.urls))
]
