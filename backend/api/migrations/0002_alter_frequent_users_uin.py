# Generated by Django 3.2.5 on 2021-11-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequent_users',
            name='UIN',
            field=models.IntegerField(unique=True),
        ),
    ]
