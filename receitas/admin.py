from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    #Listando no Display do Admin nome_receita e Categoria também listando pelos links

    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    list_display_links = ('id','nome_receita')
    search_fields = ('nome_receita',) #Buscando nome receita
    list_filter = ('categoria',) #listando por categoria
    list_editable = ('publicada' ,) #Editando direto no adm sem com checkbox.
    list_per_page = 15 #Listando por número de receita por páginas.


admin.site.register(Receita, ListandoReceitas)

