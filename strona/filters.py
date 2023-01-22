import django_filters

from .models import *

class OgloszenieFilter(django_filters.FilterSet):
    class Meta:
        model = Ogloszenie
        fields = ['przedmiot','zakres_materialu','zagadnienie']

class NauczajOgloszenieFilter(django_filters.FilterSet):
    class Meta:
        model = NauczajOgloszenie
        fields = ['przedmiot','zakres_od','zakres_do']