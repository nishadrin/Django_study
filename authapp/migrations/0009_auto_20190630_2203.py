# Generated by Django 2.2.2 on 2019-06-30 22:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20190630_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 2, 22, 3, 19, 792744, tzinfo=utc)),
        ),
    ]