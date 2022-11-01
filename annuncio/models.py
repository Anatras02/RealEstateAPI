from django.db import models

from RealEstateAPI.functions import upload_to
from agenzia_immobiliare.models import AgenziaImmobiliare
from indirizzo.models import Indirizzo


class TipologiaImmobile(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class ContrattoImmobile(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class FotoImmobile(models.Model):
    foto = models.ImageField(upload_to=upload_to("images/annunci"))


class Annuncio(models.Model):
    titolo = models.CharField(max_length=100)
    descrizione = models.TextField()
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    superficie = models.IntegerField()
    numero_vani = models.IntegerField()
    numero_bagni = models.IntegerField()
    numero_camere = models.IntegerField()
    numero_piani = models.IntegerField()
    piano = models.IntegerField()
    data_inserimento = models.DateTimeField(auto_now_add=True)
    data_modifica = models.DateTimeField(auto_now=True)

    indirizzo = models.ForeignKey(Indirizzo, on_delete=models.CASCADE)
    agenzia = models.ForeignKey(AgenziaImmobiliare, on_delete=models.CASCADE)
    tipologie = models.ManyToManyField(TipologiaImmobile)
    contratto = models.ForeignKey(ContrattoImmobile, on_delete=models.CASCADE)
    foto = models.ManyToManyField(FotoImmobile)
