# Generated by Django 3.1.7 on 2021-06-15 21:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_auto_20210615_0900'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('user', 'course')},
        ),
    ]