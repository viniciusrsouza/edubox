# Generated by Django 3.1.7 on 2021-06-27 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20210623_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='teacher',
        ),
    ]
