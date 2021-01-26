from django.db import models

class RodzajDan(models.Model):
    nazwa = models.CharField(max_length=45,unique=True)

    class Meta:
        ordering = ('nazwa',)

    def __str__(self):
        return self.nazwa


class Danie(models.Model):
    nazwa = models.CharField(max_length=45)
    rodzajDania = models.ForeignKey(RodzajDan, related_name='danie', on_delete=models.CASCADE)
    dataDodaniaDania = models.DateTimeField(auto_now_add=True)
    przepis = models.CharField(max_length=2500)
    czasPrzygotowania = models.IntegerField()
    cena = models.DecimalField(max_digits=14, decimal_places=2)
    User = models.ForeignKey('auth.User', related_name='danie', on_delete=models.CASCADE)

    class Meta:
        ordering = ('nazwa',)

    def __str__(self):
        return self.nazwa

class Klient(models.Model):
    Mezczyzna = 'M'
    Kobieta = 'K'
    wyborPlci = ((Mezczyzna, 'Mezczyzna'), (Kobieta,'Kobieta'),)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    plec = models.CharField(max_length=2, choices=wyborPlci, default=Mezczyzna)
    adres = models.CharField(max_length=45)
    dataUrodzenia = models.DateField()
    dataRejestracji = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return self.imie+' '+self.nazwisko


class Zamowienie(models.Model):
    klient = models.ForeignKey(Klient, related_name='zamowienie', on_delete=models.CASCADE)
    danie = models.ForeignKey(Danie, related_name='zamowienie', on_delete=models.CASCADE)
    cena = models.DecimalField(max_digits=14, decimal_places=2)
    ilosc = models.IntegerField()

