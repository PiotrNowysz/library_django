from django.shortcuts import render, redirect
from django.views import View
from books.models import Book, BookUser, Author
import operator
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from books import forms as books_forms
from django.db.models import Q
from books import filters
from books import validors



# Create your views here.

class BooksListView(View):
    def get(self, request):
        books = sorted(Book.objects.all(), key=operator.attrgetter('title'))
        return render(request, 'books/books_list.html', {'books': books})

    def post(self, request):
        search = request.POST.get('search')
        print(search)
        books = sorted(Book.objects.filter(
            Q(author__first_name__icontains=search) | Q(author__last_name__icontains=search) | Q(
                title__icontains=search)), key=operator.attrgetter('title'))

        return render(request, 'books/books_list.html', {'books': books})


class BookDetailsView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        user = request.user
        validation = validors.validate_renting(book, user)

        return render(request, 'books/book_details.html', {'book': book,
                                                           'validation': validation})


class BookRentView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        user = request.user
        book = Book.objects.get(id=book_id)
        if validors.validate_renting(book, user):
            BookUser(user=user, book=book, deadline=timezone.now() + timedelta(days=12), is_rented=True).save()
            book.current_store -= 1
            book.save()
            return redirect('/user/')
        else:
            return redirect('/')


class BookReturnView(PermissionRequiredMixin, View):
    permission_required = 'auth.change_book'
    permission_denied_message = _('access denied')

    def get(self, request, bookuser_id):
        bookuser = BookUser.objects.get(id=bookuser_id)
        bookuser.is_rented = False
        bookuser.return_date = timezone.now()
        bookuser.book.current_store += 1
        bookuser.save()
        return redirect(f"/user/{bookuser.user.id}")

class BookExtendView(PermissionRequiredMixin, View):
    permission_required = 'auth.change_book'
    permission_denied_message = _('access denied')

    def get(self, request, bookuser_id):
        bookuser = BookUser.objects.get(id=bookuser_id)
        bookuser.deadline += timedelta(days=7)
        bookuser.save()
        return redirect(f"/user/{bookuser.user.id}")


class AuthorDetailsView(View):
    def get(self, request, author_id):
        author = Author.objects.get(id=author_id)
        return render(request, 'books/author_details.html', {'author': author})


class MyBooksView(LoginRequiredMixin, View):
    def get(self, request):
        bookuser_set = BookUser.objects.filter(user=request.user, is_rented=True)
        return render(request, 'books/my_books.html', {'bookuser_set': bookuser_set})


class BookAddView(PermissionRequiredMixin, View):
    permission_required = 'auth.add_book'
    permission_denied_message = _('access denied')

    def get(self, request):
        book_form = books_forms.BookForm()
        author_form = books_forms.AuthorForm()
        genre_form = books_forms.GenreFrom()
        return render(request, 'books/book_add.html', {'book_form': book_form,
                                                       'author_form': author_form,
                                                       'genre_form': genre_form})

    def post(self, request):
        if 'book_btn' in request.POST:
            form = books_forms.BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        if 'author_btn' in request.POST:
            form = books_forms.AuthorForm(request.POST)
            if form.is_valid():
                form.save()

        if 'genre_btn' in request.POST:
            form = books_forms.GenreFrom(request.POST)
            if form.is_valid():
                form.save()

        return redirect('/book_add/')


class BookEditView(PermissionRequiredMixin, View):
    permission_required = 'auth.change_book'
    permission_denied_message = _('access denied')

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        form = books_forms.BookForm(instance=book)
        return render(request, 'books/book_edit.html', {'form': form,
                                                        'book_id': book_id})

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        form = books_forms.BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')


class BookDeleteView(PermissionRequiredMixin, View):
    permission_required = 'auth.delete_book'
    permission_denied_message = _('access denied')

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect('/book_search')


class BookFilterView(View):

    def get(self, request):
        book_list = Book.objects.all()
        filter = filters.BookFilter(request.GET, queryset=book_list)
        return render(request, 'books/book_search.html', {'filter': filter})


class UserFilterView(View):

    def get(self, request):
        user_list = User.objects.all()
        filter = filters.UserFilter(request.GET, queryset=user_list)
        return render(request, 'books/users.html', {'filter': filter})


class UserDetailsView(View):

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'books/user_details.html', {'user': user})
