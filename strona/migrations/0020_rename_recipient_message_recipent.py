# Generated by Django 4.1.4 on 2023-01-14 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0019_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recipient',
            new_name='recipent',
        ),
    ]
