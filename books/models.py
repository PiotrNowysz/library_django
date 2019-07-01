from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from books.utills import get_upload_file_hashdir, make_md5

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
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    language = models.CharField(max_length=32, choices=LANGUAGES, null=True)
    store = models.IntegerField()
    current_store = models.IntegerField(blank=True, null=True)
    description = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    user = models.ManyToManyField(User, through='BookUser')
    md5_cover = models.CharField(max_length=32, blank=True)
    cover = models.ImageField(blank=True, null=True, upload_to=get_upload_file_hashdir)
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
    rating = models.IntegerField(choices=RATING,null=True, blank=True )
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.book}'