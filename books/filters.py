from django.contrib.auth.models import User
from books.models import Book
import django_filters


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'store', 'current_store', 'language', 'barcode']


class UserFilter(django_filters.FilterSet):
    book__title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'userdetails__phone_number', 'book__title']
