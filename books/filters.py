from django.contrib.auth.models import User
from django.db import models
import django.forms as forms
from books.models import Book
import django_filters
from datetime import datetime

CHOICES = (
    (None, '--------'),
    (True, 'YES'),
)


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    bookuser__is_rented = django_filters.ChoiceFilter(label="Is rented", distinct=True, choices=CHOICES,
                                                      empty_label=None)

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'store', 'current_store', 'language', 'barcode','bookuser__is_rented']


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(label='Email')
    book__title = django_filters.CharFilter(label="Rented book", distinct=True)
    bookuser__is_rented = django_filters.ChoiceFilter(label="Has rented book", distinct=True, choices=CHOICES,
                                                      empty_label=None)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'book__title', 'bookuser__is_rented']
