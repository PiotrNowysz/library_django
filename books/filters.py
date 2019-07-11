from django.contrib.auth.models import User
from books.models import Book
import django_filters
from django.utils.translation import gettext_lazy as _


CHOICES = (
    (None, '--------'),
    (True, _('YES')),
)


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label=_('Title'))
    bookuser__is_rented = django_filters.ChoiceFilter(label=_("Is rented"), distinct=True, choices=CHOICES,
                                                      empty_label=None)

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'store', 'current_store', 'language','bookuser__is_rented']


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(label=_('Email address'))
    book__title = django_filters.CharFilter(label=_("Rented book"), distinct=True)
    bookuser__is_rented = django_filters.ChoiceFilter(label=_("Has rented book"), distinct=True, choices=CHOICES,
                                                      empty_label=None)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'book__title', 'bookuser__is_rented']
