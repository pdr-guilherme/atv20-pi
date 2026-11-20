from django.db import models
from django.utils.translation import gettext_lazy as _


class Diretor(models.Model):
    nome = models.CharField(_("nome"), max_length=100, unique=True)

    class Meta:
        ordering = ("nome",)
        verbose_name = _("diretor")
        verbose_name_plural = _("diretores")

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(_("nome"), max_length=50, unique=True)

    class Meta:
        ordering = ("nome",)
        verbose_name = _("categoria")
        verbose_name_plural = _("categorias")

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(_("título"), max_length=200)
    ano_lancamento = models.PositiveSmallIntegerField(_("ano de lançamento"))
    duracao_minutos = models.PositiveSmallIntegerField(_("duração em minutos"))
    sinopse = models.TextField(_("sinopse"), blank=True)
    diretor = models.ForeignKey(
        Diretor,
        on_delete=models.PROTECT,
        related_name="filmes",
        verbose_name=_("diretor"),
    )
    categorias = models.ManyToManyField(
        Categoria,
        related_name="filmes",
        verbose_name=_("categorias"),
    )

    class Meta:
        ordering = ("titulo", "ano_lancamento")
        verbose_name = _("filme")
        verbose_name_plural = _("filmes")

    def __str__(self):
        return f"{self.titulo} ({self.ano_lancamento})"
