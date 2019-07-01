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