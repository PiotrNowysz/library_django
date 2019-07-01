import django.forms as forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .validators import validate_password
from django.core.validators import EmailValidator


class UserCreateForm(UserCreationForm):
    username = forms.EmailField(label=_('Email address'), validators=[EmailValidator()])
    first_name = forms.CharField(label=_('First Name'))
    last_name = forms.CharField(label=_('Last Name'))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput, validators=[validate_password])
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)
    permission = forms.BooleanField(label=_('I accept the terms'), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'permission')

    def clean_username(self):
        email = self.cleaned_data.get('username').strip().lower()
        return email

    def clean_permission(self):
        permission = self.cleaned_data.get('permission')
        if permission:
            return permission
        else:
            raise forms.ValidationError(_('You need to accept the terms'))


class LoginForm(forms.Form):
    username = forms.EmailField(label=_('Email address'), validators=[EmailValidator()])
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)

    def clean_username(self):
        email = self.cleaned_data.get('username').strip().lower()
        return email


class PasswordForgottenForm(forms.Form):
    email = forms.EmailField(label=_('Email address'), validators=[EmailValidator()])

    def clean_email(self):
        email = self.cleaned_data.get('email').strip().lower()
        if len(User.objects.filter(username=email)[:1]) == 0:
            raise forms.ValidationError(_('There is no user with the e-mail address provided'))
        else:
            return email


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput, validators=[validate_password])
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match")
        return cleaned_data
