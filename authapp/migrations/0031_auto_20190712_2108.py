# Generated by Django 2.2.2 on 2019-07-12 21:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0030_auto_20190711_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 21, 8, 21, 362795, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
