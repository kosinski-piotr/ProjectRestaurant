from rest_framework import serializers
from .models import Zamowienie, Danie, RodzajDan, Klient
from django.contrib.auth.models import User

class RodzajDanSerializer(serializers.HyperlinkedModelSerializer):

    danie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='danie-detail')
    class Meta:
        model = RodzajDan
        fields = ['pk','url', 'nazwa', 'danie']


class DanieSerializer(serializers.HyperlinkedModelSerializer):
    rodzajDania = serializers.SlugRelatedField(queryset=RodzajDan.objects.all(), slug_field='nazwa')
    zamowienie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zamowienie-detail')
    user = serializers.ReadOnlyField(source='User.username')
    class Meta:
        model = Danie
        fields = ['url', 'nazwa', 'rodzajDania', 'user', 'dataDodaniaDania', 'przepis', 'cena','czasPrzygotowania', 'zamowienie']

class KlientSerializer(serializers.HyperlinkedModelSerializer):
    zamowienie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zamowienie-detail')
    plec = serializers.ChoiceField(choices=Klient.wyborPlci)
    class Meta:
        model = Klient
        fields = ['url','pk','imie', 'nazwisko', 'plec', 'dataUrodzenia','dataRejestracji','zamowienie']


class ZamowienieSerializer(serializers.HyperlinkedModelSerializer):
    klient = serializers.SlugRelatedField(queryset=Klient.objects.all(), slug_field='nazwisko')
    danie =  serializers.SlugRelatedField(queryset=Danie.objects.all(), slug_field='nazwa')
    class Meta:
        model = Zamowienie
        fields = ['pk','url','klient','danie','cena', 'ilosc']

class UserDanieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Danie
        fields = ['url','nazwa']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    dania = UserDanieSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['url','pk','username','dania']
