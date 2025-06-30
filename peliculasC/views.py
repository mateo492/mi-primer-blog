from django.shortcuts import render
from .models import Publicacion1

def lista_public1(request):
    peliculas = Publicacion1.objects.all()        # ya vienen ordenadas
    return render(request, "peliculas/lista_peliculas.html",
                  {"peliculas": peliculas})