from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import UserDetails
from . import forms
from django.contrib import auth
from django.utils.translation import gettext as _


# Create your views here.
class UserCreateView(View):
    def get(self, request):
        user_form = forms.UserCreateForm()

        return render(request, 'registration/user_create.html', {'user_form': user_form, })

    def post(self, request):
        user_form = forms.UserCreateForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
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
                return redirect("/home")
            except AttributeError:
                return render(request, 'registration/login.html', {'form': form,
                                                                   'message': _('Wrong email or password')})

        else:
            return render(request, 'registration/login.html', {'form': form})