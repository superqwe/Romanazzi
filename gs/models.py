from django.db import models


# Create your models here.
class Cliente(models.Model):
    ragione_sociale = models.CharField(max_length=100)
    partita_iva = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pec = models.EmailField(blank=True, null=True)
    indirizzo = models.CharField(max_length=200, blank=True, null=True)
    citta = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=2, blank=True, null=True)
    cap = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    riferimento = models.CharField(max_length=100, blank=True, null=True)
    # codice_ateco
    numero_REA = models.CharField(max_length=20, blank=True, null=True)
    posizione_INPS = models.CharField(max_length=20, blank=True, null=True)
    posizione_INAIL = models.CharField(max_length=20, blank=True, null=True)
    cassa_edile = models.CharField(max_length=20, blank=True, null=True)
    incarico_RSPP_esterno = models.BooleanField(default=False)
    data_contratto = models.DateField(blank=True, null=True)
    data_scadenza_contratto = models.DateField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    cessato = models.BooleanField(default=False)
