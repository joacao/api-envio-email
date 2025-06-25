from django.db import models

class Cliente(models.Model):

    nome = models.CharField(null=False, blank=False, max_length=75)
    email = models.EmailField(null=False, blank=False,max_length=75)
    telefone = models.CharField(null=False, blank=False, max_length=11)
    telefone_whatsapp = models.BooleanField(null=False, blank=False)
    endereco = models.CharField(null=False, blank=False, max_length=100)
    numero_endereco = models.CharField(null=False, blank=False, max_length=5)
    cidade = models.CharField(null=False, blank=False, max_length=23)
    estado = models.CharField(null=False, blank=False, max_length=2)
    cep = models.CharField(null=False, blank=False, max_length=8)

    def __str__(self):
        return self.nome

class Envio(models.Model):
    cliente = models.ForeignKey(Cliente,null=False, blank=False, on_delete=models.CASCADE)
    status_envio = models.CharField(null=False, blank=False, max_length=50)
    texto = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.cliente} - {self.status_envio}'