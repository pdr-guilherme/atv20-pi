from django.contrib import admin

from core.models import Categoria, Diretor, Filme


@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "ano_lancamento", "diretor")
    filter_horizontal = ("categorias",)
