# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # usá el nombre real de la vista:
    path('', views.lista_public, name='lista_peliculas'),
]