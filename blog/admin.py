# blog/admin.py
from django.contrib import admin
from .models import Publicacion

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display  = ("titulo", "anio", "autor")
    search_fields = ("titulo",)