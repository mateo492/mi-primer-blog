from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('evaluacion2/', include('blog.urls')),  # prefijo evaluacion2
]

