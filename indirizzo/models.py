from django.db import models


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
