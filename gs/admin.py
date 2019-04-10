from django.contrib import admin

from .models import Cliente, Codice_Ateco
# Register your models here.

class Codice_Ateco_Admin(admin.ModelAdmin):
    list_display = ['codice', 'descrizione', 'classe_di_rischio']

admin.site.register(Cliente)
admin.site.register(Codice_Ateco, Codice_Ateco_Admin)