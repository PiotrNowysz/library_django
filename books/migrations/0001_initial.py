# Generated by Django 2.2.3 on 2019-07-04 16:14

import books.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(null=True)),
                ('language', models.CharField(choices=[('en', 'english'), ('pl', 'polish'), ('fr', 'french'), ('es', 'spanish'), ('de', 'german')], max_length=32, null=True)),
                ('store', models.IntegerField()),
                ('current_store', models.IntegerField(blank=True, null=True)),
                ('md5_cover', models.CharField(blank=True, max_length=32)),
                ('cover', models.ImageField(upload_to=books.utils.get_upload_file_hashdir)),
                ('barcode', models.CharField(blank=True, max_length=256)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='BookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=1024, null=True)),
                ('rating', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('is_rented', models.BooleanField(default=False)),
                ('rent_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='books.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ManyToManyField(through='books.BookUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
