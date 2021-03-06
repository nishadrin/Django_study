# Generated by Django 2.2.2 on 2019-06-29 22:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20190629_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 1, 22, 29, 26, 452134, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
