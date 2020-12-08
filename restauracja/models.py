from django.db import models

class Klient(models.Model):
    idKlient=models.AutoField(primary_key=True)
    email=models.CharField(max_length=45,null=False)
    haslo=models.CharField(max_length=45,null=False)
    adres=models.CharField(max_length=45,null=False)
    nrTelefonu=models.IntegerField(max_length=9, null=False)

class Zamowienie(models.Model):
    idZamowienie=models.AutoField(primary_key=True)
    dania=models.CharField(max_length=200, null=False)
    dataZamowienia=models.DateField(null=False)
    kwota=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    klient=models.ForeignKey(Klient, on_delete=models.CASCADE)

class Platnosc(models.Model):

    naMiejscu='Na_miejscu'
    przelew='przelew'
    rodzaj_platnosci = (
        (naMiejscu, 'Na_miejscu'),
        (przelew, 'Przelew'),
        )
    idPlatnosc=models.AutoField(primary_key=True)
    rodzaj=models.CharField(max_length=10,choices=rodzaj_platnosci,default=przelew)
    zamowienie=models.ForeignKey(Zamowienie, on_delete=models.CASCADE)

class Restauracja(models.Model):
    idRestauracja=models.AutoField(primary_key=True)
    nazwa= models.CharField(max_length=45,null=False)
    adres=models.CharField(max_length=45,null=False)

class Danie(models.Model):
    idDanie=models.AutoField(primary_key=True)
    nazwa=models.CharField(max_length=45,null=False)
    cena=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    restauracja=models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    zamowienie=models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
# Create your models here.
