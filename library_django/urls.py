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
    re_path(r'^reset/(?P<user_id>(\d)+)/(?P<token>(\w)+)', registration_views.ResetPasswordView.as_view(), name='reset_password'),
    re_path(r'^book/(?P<book_id>(\d)+)', books_views.BookDetailsView.as_view(), name='book_details'),
    path('home/', books_views.BooksListView.as_view(), name='main'),
    re_path(r'^reserve/(?P<book_id>(\d)+)', books_views.BookReserveView.as_view(), name='reserve'),

]
