# Generated by Django 3.2.5 on 2021-11-24 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20211124_1030'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Error',
        ),
        migrations.AlterField(
            model_name='guest',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 10, 35, 24, 870368)),
        ),
    ]
