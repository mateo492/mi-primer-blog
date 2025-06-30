from django.shortcuts import render
from .models import Publicacion

def lista_public(request):
    peliculas = Publicacion.objects.all()        # ya vienen ordenadas
    return render(request, "peliculas/lista_peliculas.html",
                  {"peliculas": peliculas})