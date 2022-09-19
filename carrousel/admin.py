from django.contrib import admin
from .models import CarrouselIntroduccion

class CarrouselIntroduccionadmin(admin.ModelAdmin):

    list_display = ["orden", "descripcion"]

admin.site.register(CarrouselIntroduccion, CarrouselIntroduccionadmin)