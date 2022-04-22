from django.contrib import admin

from escola.models import Aluno, Aula

# Register your models here.


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'presente_aula')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


class Aulas(admin.ModelAdmin):

    search_fields = ('nome',)




admin.site.register(Aula, Aulas)
admin.site.register(Aluno, Alunos)