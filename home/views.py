from django.shortcuts import render
from carrousel.models import CarrouselIntroduccion


def home(request):
    params = {}
    carrou_intro = CarrouselIntroduccion.objects.filter()
    params["carrou_intro"] = carrou_intro

    return render(request, "principal/home.html", params)


def comuna(request):
    params = {}

    return render(request, "principal/comuna.html", params)