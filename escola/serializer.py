
from dataclasses import field
from django.forms import Field
from rest_framework import serializers
from escola.models import Aluno, Aula



class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'presente_aula', 'aula']

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        field = ['nome']
