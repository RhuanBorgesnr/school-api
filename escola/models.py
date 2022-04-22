from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    presente_aula = models.BooleanField(default=False)
    aula = models.ManyToManyField("Aula", related_name="alunos")

    def __str__(self):
        return self.nome



class Aula(models.Model):
    nome = models.CharField(max_length=30)
    aluno = models.ManyToManyField(Aluno, related_name="aulas")


    def __str__(self):
        return self.nome


