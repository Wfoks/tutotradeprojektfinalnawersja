# Generated by Django 4.1.4 on 2023-01-09 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0007_friend_userprofile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='my_friends', to='strona.friend'),
        ),
    ]