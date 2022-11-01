from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from RealEstateAPI.functions import upload_to


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
