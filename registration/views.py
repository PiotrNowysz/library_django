from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib import auth
from django.utils.translation import gettext as _
from django.utils import timezone
from datetime import timedelta
from .utills import send_mail_to
from django.utils.crypto import get_random_string
from registration.models import UserDetails
from django.http import JsonResponse


# Create your views here.
class UserCreateView(View):
    def get(self, request):
        user_form = forms.UserCreateForm()
        return render(request, 'registration/user_create.html', {'user_form': user_form})

    def post(self, request):
        user_form = forms.UserCreateForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            UserDetails.objects.create(user=user)
            return redirect('/login/')
        else:
            return render(request, 'registration/user_create.html', {'user_form': user_form})


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(username=username, password=password)
            try:
                auth.login(request, user)
                return redirect("/")
            except AttributeError:
                return render(request, 'registration/login.html', {'form': form,
                                                                   'message': _('Wrong email or password')})

        else:
            return render(request, 'registration/login.html', {'form': form})


class PasswordForgottenView(View):

    def get(self, request):
        form = forms.PasswordForgottenForm()
        return render(request, 'registration/email_form.html', {'form': form})

    def post(self, request):
        form = forms.PasswordForgottenForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            token = get_random_string(length=32)
            user = User.objects.get(username=email)
            user.userdetails.hash = token
            user.userdetails.hash_valid_to = timezone.now() + timedelta(hours=2)
            user.userdetails.save()
            send_mail_to("Zmiana hasła", email, f'http://127.0.0.1:8000/reset/{user.id}/{token}')

            return render(request, 'registration/email_form.html', {'form': form,
                                                                    'message': _('We sent you an email')})
        return render(request, 'registration/email_form.html', {'form': form})


class ResetPasswordView(View):
    def get(self, request, user_id, token):
        user = User.objects.get(id=user_id)
        form = forms.PasswordResetForm()
        if user.userdetails.hash == token and user.userdetails.hash_valid_to > timezone.now():
            return render(request, 'registration/reset_password.html',
                          {'form': form, 'user_id': user_id, 'token': token})
        else:
            return render(request, 'registration/reset_password.html',
                          {'message': 'this link has expired', 'user_id': user_id, 'token': token})

    def post(self, request, user_id, token):
        form = forms.PasswordResetForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=user_id)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('/login/')
        return render(request, 'registration/reset_password.html',
                      {'form': form, 'user_id': user_id, 'token': token})


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
