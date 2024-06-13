from django.contrib import admin
from django.urls import path
from . import views  # Asegúrate de importar views desde el directorio actual

urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
