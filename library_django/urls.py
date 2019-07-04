"""library_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from registration import views as registration_views
from django.contrib.auth.views import LogoutView
from books import views as books_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_views.UserCreateView.as_view(), name='register'),
    path('login/', registration_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_forgotten/', registration_views.PasswordForgottenView.as_view(), name='password_forgotten'),
    re_path(r'^reset/(?P<user_id>(\d)+)/(?P<token>(\w)+)', registration_views.ResetPasswordView.as_view(),
            name='reset_password'),
    re_path(r'^book/(?P<book_id>(\d)+)', books_views.BookDetailsView.as_view(), name='book_details'),
    path('', books_views.BooksListView.as_view(), name='home'),
    re_path(r'^reserve/(?P<book_id>(\d)+)', books_views.BookRentView.as_view(), name='reserve'),
    re_path(r'^author/(?P<author_id>(\d)+)', books_views.AuthorDetailsView.as_view(), name='author_details'),
    path('user/', books_views.MyBooksView.as_view(), name='my_books'),
    re_path(r'^users/$', books_views.UserFilterView.as_view(), name='users'),
    path('book_add/', books_views.BookAddView.as_view(), name='book_add'),
    re_path(r'^book_edit/(?P<book_id>(\d)+)', books_views.BookEditView.as_view(), name="book_edit"),
    re_path(r'^book_delete/(?P<book_id>(\d)+)', books_views.BookDeleteView.as_view(), name="book_delete"),
    re_path(r'^book_search/$', books_views.BookFilterView.as_view(), name='book_search'),
    re_path(r'^user/(?P<user_id>(\d)+)', books_views.UserDetailsView.as_view(), name='user_details')
]
