from django.shortcuts import render
from django.views import View
from .models import Book, BookUser
import operator


# Create your views here.

class BooksListView(View):
    def get(self, request):
        books = sorted(Book.objects.all(), key=operator.attrgetter('title'))
        return render(request, 'books/books_list.html', {'books': books})


class BookDetailsView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        return render(request, 'books/book_details.html', {'book': book})