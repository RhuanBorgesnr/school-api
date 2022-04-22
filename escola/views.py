from rest_framework import viewsets
from escola.models import Aluno, Aula
from escola.serializer import AlunoSerializer, AulaSerializer
from django.shortcuts import render, get_list_or_404, get_object_or_404


# class Alunoslist(viewsets.ModelViewSet):

def aulas(request):
    
        aulas = Aula.objects.all()
        objects = Aluno.objects.all()
        context = {
                'aulas': aulas, 
                'objects': objects}
        return render(request, "list.html", context )


def alunos(request):
        if 'presente_aula' in request.POST:
            lista_presenca = request.POST['presente_aula']
        else:
            lista_presenca = False
        alunos = Aluno.objects.all()
      
        search = request.GET.get('search')
        if search:
            alunos = Aluno.objects.filter(nome__icontains=search)
        context={"alunos": alunos, "aulas": aulas}

        return render(request, 'index.html', context)


class AlunosViewSet(viewsets.ModelViewSet):
        queryset = Aluno.objects.all()
        serializer_class = AlunoSerializer


class AulaViewSet(viewsets.ModelViewSet):
        queryset = Aula.objects.all()
        serializer_class = AulaSerializer


