from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from tutotradeproject import settings

# Create your models here.

class Ogloszenie(models.Model):
    PRZEDMIOT = (
        ('Matematyka', 'Matematyka'),
        ('Język polski', 'Język polski'),
        ('Język angielski', 'Język angielski'),
    )
    ZAKRES = (
        ('6 podstawówka', '6 podstawówka'),
        ('7 podstawówka', '7 podstawówka'),
        ('8 podstawówka', '8 podstawówka'),
        ('1 liceum', '1 liceum'),
        ('2 liceum', '2 liceum'),
        ('3 liceum', '3 liceum'),
        ('4 liceum', '4 liceum'),
    )

    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    przedmiot = models.CharField(max_length=20, null=True, choices=PRZEDMIOT)
    zakres_materialu = models.CharField(max_length=20, null=True, choices=ZAKRES)
    zagadnienie = models.CharField(max_length=100, null=True)
    data = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.zagadnienie



class NauczajOgloszenie(models.Model):
    PRZEDMIOT = (
        ('Matematyka', 'Matematyka'),
        ('Język polski', 'Język polski'),
        ('Język angielski', 'Język angielski'),
    )
    ZAKRES = (
        ('6 podstawówka', '6 podstawówka'),
        ('7 podstawówka', '7 podstawówka'),
        ('8 podstawówka', '8 podstawówka'),
        ('1 liceum', '1 liceum'),
        ('2 liceum', '2 liceum'),
        ('3 liceum', '3 liceum'),
        ('4 liceum', '4 liceum'),
    )


    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    przedmiot = models.CharField(max_length=20, null=True, choices=PRZEDMIOT)
    zakres_od = models.CharField(max_length=20, null=True, choices=ZAKRES)
    zakres_do = models.CharField(max_length=20, null=True, choices=ZAKRES)
    data = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.zagadnienie

class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    has_unread = models.BooleanField(default=False)
    
class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/message_photos', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)




        