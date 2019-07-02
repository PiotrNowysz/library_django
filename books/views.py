from django.shortcuts import render, redirect
from django.views import View
from .models import Book, BookUser, Author
import operator
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BooksListView(View):
    def get(self, request):
        books = sorted(Book.objects.all(), key=operator.attrgetter('title'))
        return render(request, 'books/books_list.html', {'books': books})


class BookDetailsView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        return render(request, 'books/book_details.html', {'book': book})


class BookReserveView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        user = request.user
        book = Book.objects.get(id=book_id)
        if book.current_store < 1:
            return redirect('/')
        BookUser(user=user, book=book, deadline=timezone.now() + timedelta(days=12)).save()
        book.current_store -= 1

        book.save()
        return redirect('/user/')


class AuthorDetailsView(View):
    def get(self, request, author_id):
        author = Author.objects.get(id=author_id)
        return render(request, 'books/author_details.html', {'author': author})

class MyBooksView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'books/my_books.html', {'user': request.user})