from django.contrib import admin
from django.urls import path

from Proyecto1.view import saludar, saludar_con_fecha, saludar_a_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludar),
    path("saludo-hoy/", saludar_con_fecha),
    path("hello/<nombre>/", saludar_a_usuario),
]
