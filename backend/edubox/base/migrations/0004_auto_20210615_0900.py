# Generated by Django 3.1.7 on 2021-06-15 12:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_auto_20210614_2344'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participants',
            new_name='Membership',
        ),
        migrations.AddField(
            model_name='course',
            name='members',
            field=models.ManyToManyField(through='base.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]