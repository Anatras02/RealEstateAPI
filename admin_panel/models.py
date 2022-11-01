import os

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def upload_to(path):
    def inner_upload_to(instance, filename):
        return os.path.join(path, instance.id)

    return inner_upload_to


class Regione(models.Model):
    codice_istat = models.CharField(max_length=2, primary_key=True)
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Provincia(models.Model):
    codice_istat = models.CharField(max_length=4, primary_key=True)
    nome = models.CharField(max_length=50)
    regione = models.ForeignKey(Regione, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Comune(models.Model):
    codice_istat = models.CharField(max_length=6, primary_key=True)
    nome = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Quartiere(models.Model):
    nome = models.CharField(max_length=50)
    comune = models.ForeignKey(Comune, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Indirizzo(models.Model):
    via = models.CharField(max_length=50)
    civico = models.CharField(max_length=10)
    quartiere = models.ForeignKey(Quartiere, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.via} {self.civico}"


class AgenziaImmobiliare(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    ragione_sociale = models.CharField(max_length=100)
    nome_agenzia = models.CharField(max_length=100)
    partita_iva = models.CharField(max_length=11, unique=True, null=True, blank=True)
    codice_fiscale = models.CharField(max_length=16, unique=True, null=True, blank=True)
    logo = models.ImageField(upload_to=upload_to("images/loghi"), blank=True)

    def __str__(self):
        return self.ragione_sociale


class PermessiAgenteAgenzia(models.Model):
    permesso = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    agente_imobiliare = models.ForeignKey(User, on_delete=models.CASCADE)
    agenzia_immobiliare = models.ForeignKey(AgenziaImmobiliare, on_delete=models.CASCADE)


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
