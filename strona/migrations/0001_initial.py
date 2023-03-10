# Generated by Django 4.1.4 on 2022-12-31 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ogloszenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('przedmiot', models.CharField(choices=[('Matematyka', 'Matematyka'), ('Język polski', 'Język polski'), ('Język angielski', 'Język angielski')], max_length=20, null=True)),
                ('zakres', models.CharField(choices=[('6 podstawówka', '6 podstawówka'), ('7 podstawówka', '7 podstawówka'), ('8 podstawówka', '8 podstawówka'), ('1 liceum', '1 liceum'), ('2 liceum', '2 liceum'), ('3 liceum', '3 liceum'), ('4 liceum', '4 liceum')], max_length=20, null=True)),
                ('zagadnienie', models.CharField(max_length=100, null=True)),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
