from django.conf import settings
from django.db import models


class Publicacion1(models.Model):
    autor       = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Autor"
    )
    titulo      = models.CharField("Título", max_length=200, null=True, blank=True)
    anio        = models.PositiveSmallIntegerField("Año", null=True, blank=True)
    sinopsis    = models.TextField("Sinopsis", null=True, blank=True)
    imagen_url  = models.URLField("URL de la imagen", max_length=500, null=True, blank=True)

    # solo guardamos la fecha-hora de creación automática
    hora_creacion = models.DateTimeField(
        "Creada el",
        auto_now_add=True
    )

    class Meta:
        # ahora ordenamos por la más reciente creación
        ordering = ["-hora_creacion"]

    def __str__(self):
        return f"{self.titulo} ({self.anio})"