# Generated by Django 2.2.3 on 2019-07-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookuser',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]