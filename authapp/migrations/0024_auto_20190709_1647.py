# Generated by Django 2.2.2 on 2019-07-09 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0023_auto_20190709_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 16, 47, 31, 929022, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]