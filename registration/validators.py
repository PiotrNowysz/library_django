from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


def validate_password(password):
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@!#$%^&*()?><:"{}])[A-Za-z\d@!#$%^&*()?><:"{}]{8,}$', password):
        raise ValidationError(_(
            'Password requires minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character'))
