print("Cargando archivo principal de URLs")

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('evaluacion2', include('peliculasC.urls')),
]
