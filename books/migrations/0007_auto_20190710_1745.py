# Generated by Django 2.2.3 on 2019-07-10 17:45

import books.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20190710_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to=books.utils.get_upload_file_hashdir, verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='current_store',
            field=models.IntegerField(blank=True, null=True, verbose_name='Current store'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('en', 'angielski'), ('pl', 'polski'), ('fr', 'francuzki'), ('es', 'hiszpański'), ('de', 'niemiecki')], max_length=32, null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='book',
            name='store',
            field=models.IntegerField(verbose_name='Store'),
        ),
        migrations.AlterModelTable(
            name='author',
            table=None,
        ),
    ]