# Generated by Django 4.1.4 on 2023-01-10 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0010_remove_userprofile_tokens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
