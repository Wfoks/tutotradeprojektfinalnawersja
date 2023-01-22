# Generated by Django 4.1.4 on 2023-01-11 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('strona', '0013_remove_userprofile_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tokens',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='NauczajOgloszenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('przedmiot', models.CharField(choices=[('Matematyka', 'Matematyka'), ('Język polski', 'Język polski'), ('Język angielski', 'Język angielski')], max_length=20, null=True)),
                ('zakres', models.CharField(choices=[('6 podstawówka', '6 podstawówka'), ('7 podstawówka', '7 podstawówka'), ('8 podstawówka', '8 podstawówka'), ('1 liceum', '1 liceum'), ('2 liceum', '2 liceum'), ('3 liceum', '3 liceum'), ('4 liceum', '4 liceum')], max_length=20, null=True)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
