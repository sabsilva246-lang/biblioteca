from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Genero, Livro

# 1. Configuração do Inline (O formulário que aparece dentro dos outros)
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1  # Número de linhas vazias para novos livros

# 2. Configuração dos ModelAdmins
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome',)
    inlines = [LivroInline] # Permite ver os livros do autor na página do autor

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome',)
    inlines = [LivroInline] # Permite ver os livros da editora na página da editora

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [LivroInline] # Permite ver os livros por gênero na página do gênero

# 3. Registro dos Modelos
admin.site.register(Cidade)
admin.site.register(Leitor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Genero, GeneroAdmin)

# Nota: O Livro já é gerenciado pelos Inlines acima, 
# mas registramos ele aqui para ele ter sua própria página de listagem também.
admin.site.register(Livro)