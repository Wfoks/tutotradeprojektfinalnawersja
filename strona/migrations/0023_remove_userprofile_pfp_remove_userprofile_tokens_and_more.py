# Generated by Django 4.1.4 on 2023-01-15 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0022_threadmodel_has_unread'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pfp',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='tokens',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='static/images/profile_pictures/twojekonto-ikona_czarna.png', upload_to='static/images/profile_pictures'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]