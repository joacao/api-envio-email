from rest_framework import serializers
from send_email.models import Cliente,Envio
from send_email.validators import nome_invalido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nome','email','telefone','telefone_whatsapp','endereco','numero_endereco','cidade','estado','cep']

    def validate(self,dados):
        if nome_invalido(dados['cpf']):
            raise serializers.ValidationError({'nome':'O nome só pode conter letras!'})
        return dados
    
class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__'