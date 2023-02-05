from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):

    return render(request, "GuitarraWebApp/inicio.html")


def temas(request):

    return render(request, "GuitarraWebApp/temas.html")


def cursos(request):

    return render(request, "GuitarraWebApp/cursos.html")

def blog(request):

    return render(request, "GuitarraWebApp/productos.html")

def contacto(request):

    return render(request, "GuitarraWebApp/contacto.html")


