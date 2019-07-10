from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from books.utils import get_upload_file_hashdir, make_md5

# Create your models here.

LANGUAGES = (
    ('en', _('english')),
    ('pl', _('polish')),
    ('fr', _('french')),
    ('es', _('spanish')),
    ('de', _('german'))
)
RATING = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

class Author(models.Model):
    first_name = models.CharField(_('First name'), max_length=128)
    last_name = models.CharField(_('Last name'), max_length=128)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Genre(models.Model):
    name = models.CharField(_('Genre'), max_length=64, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(_('Description'), null=True)
    genre = models.ManyToManyField(Genre)
    language = models.CharField(_('Language'), max_length=32, choices=LANGUAGES, null=True)
    store = models.IntegerField(_('Store'), )
    current_store = models.IntegerField(_('Current store'), blank=True, null=True)
    user = models.ManyToManyField(User, through='BookUser')
    md5_cover = models.CharField(max_length=32, blank=True)
    cover = models.ImageField(_('Cover'), upload_to=get_upload_file_hashdir)
    barcode = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.md5 = make_md5(self.cover.file)
        if self.current_store is None:
            self.current_store = self.store
        super(Book, self).save(*args, **kwargs)


class BookUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024, null=True, blank=True)
    rating = models.IntegerField(choices=RATING, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_rented = models.BooleanField(default=False)
    rent_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.book}'
