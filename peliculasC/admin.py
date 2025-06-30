# blog/admin.py
from django.contrib import admin
from .models import Publicacion1

@admin.register(Publicacion1)
class PublicacionAdmin(admin.ModelAdmin):
    list_display  = ("titulo", "anio", "autor")
    search_fields = ("titulo",)