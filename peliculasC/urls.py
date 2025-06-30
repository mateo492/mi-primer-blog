from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_public1, name='lista_peliculas'),
]