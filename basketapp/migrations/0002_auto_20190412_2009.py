# Generated by Django 2.2 on 2019-04-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='количество'),
        ),
    ]
