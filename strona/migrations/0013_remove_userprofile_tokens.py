# Generated by Django 4.1.4 on 2023-01-10 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0012_userprofile_tokens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='tokens',
        ),
    ]
