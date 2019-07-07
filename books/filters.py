from django.contrib.auth.models import User
from books.models import Book
import django_filters


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'store', 'current_store', 'language', 'barcode']


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(label='Email')
    book__title = django_filters.CharFilter(label="Rented book")
    bookuser__is_rented = django_filters.BooleanFilter(label="Has rented book")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'book__title', 'bookuser__is_rented']
