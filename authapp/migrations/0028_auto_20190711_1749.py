# Generated by Django 2.2.2 on 2019-07-11 17:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0027_auto_20190711_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 13, 17, 49, 28, 406603, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
