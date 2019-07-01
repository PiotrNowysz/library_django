from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    hash = models.TextField(blank=True, null=True)
    hash_valid_to = models.DateTimeField(blank=True, null=True)
