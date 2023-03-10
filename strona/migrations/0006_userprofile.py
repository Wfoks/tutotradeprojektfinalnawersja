# Generated by Django 4.1.4 on 2023-01-08 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('strona', '0005_ogloszenie_author_ogloszenie_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('pfp', models.ImageField(blank=True, default='static/images/twojekonto-ikona_czarna.png', upload_to='uploads/profile_pictures')),
            ],
        ),
    ]
