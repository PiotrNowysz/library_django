from books.models import Book, BookUser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def validate_renting(book, user):
    book_user_set = BookUser.objects.filter(user=user)
    if book.current_store < 1:
        return False
    try:
        if book_user_set.get(book=book, is_rented=True).is_rented:
            return False
    except ObjectDoesNotExist:
        pass
    return True
