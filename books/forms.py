import django.forms as forms
import books.models as models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        exclude = ['current_store', 'user', 'md5_cover', 'barcode']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'


class GenreFrom(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'
