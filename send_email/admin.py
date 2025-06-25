from django.contrib import admin
from send_email.models import Cliente, Envio

class Clientes(admin.ModelAdmin):
    list_display = ('id','nome','email','telefone','telefone_whatsapp','endereco','numero_endereco','cidade','estado','cep',)
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(Cliente,Clientes)

class Envios(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'status_envio', 'texto',)
    list_display_links = ('id', 'cliente',)
    search_fields = ('cliente',)
    list_per_page = 20

admin.site.register(Envio,Envios)

