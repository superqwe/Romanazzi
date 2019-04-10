from django.db import models


class Codice_Ateco(models.Model):
    codice = models.CharField(max_length=8, unique=True)
    descrizione = models.CharField(max_length=100, blank=True, null=True)
    classe_di_rischio = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.codice, self.descrizione)

    class Meta:
        ordering = ['codice', ]
        verbose_name = 'Codice Ateco'
        verbose_name_plural = 'Codici Ateco'


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
    codice_ateco = models.ForeignKey(Codice_Ateco, on_delete=models.CASCADE, blank=True, null=True,)
    numero_REA = models.CharField(max_length=20, blank=True, null=True)
    posizione_INPS = models.CharField(max_length=20, blank=True, null=True)
    posizione_INAIL = models.CharField(max_length=20, blank=True, null=True)
    cassa_edile = models.CharField(max_length=20, blank=True, null=True)
    incarico_RSPP_esterno = models.BooleanField(default=False)
    data_contratto = models.DateField(blank=True, null=True)
    data_scadenza_contratto = models.DateField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    cessato = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.ragione_sociale

    class Meta:
        ordering = ['ragione_sociale', ]
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clienti'
