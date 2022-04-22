from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from escola.models import *



class AlunosForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"

