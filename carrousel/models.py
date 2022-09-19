from django.db import models


class CarrouselIntroduccion(models.Model):

    UNO = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    ORDEN = (
        (UNO, 1),
        (DOS, 2),
        (TRES, 3),
        (CUATRO, 4),
    )

    orden = models.IntegerField(choices=ORDEN, default=UNO)
    imagen = models.ImageField(
        upload_to="carrouselle_intro/%Y/%m/%d", blank=True, null=True
    )
    titulo = models.CharField(
        "Titulo", max_length=50, blank=True, null=True
    )
    descripcion = models.CharField(
        "Descripcion (220)", max_length=220, blank=True, null=True
    )
    ir_a = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Introducción Carrouselle"
        verbose_name_plural = "Introducción Carrouselle"
