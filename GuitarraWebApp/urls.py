from django.urls import path

from GuitarraWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('temas', views.temas, name="Temas"),
    path('cursos', views.cursos, name="Cursos"),
    path('productos', views.blog, name="Productos"),
    path('contacto', views.contacto, name="Contacto"),

]