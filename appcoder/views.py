from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"appcoder/inicio.html")
def estudiante(request):
    return render(request,"appcider/cursos.html")
def profesor(request):
    return HttpResponse("Vista de profesores")
def cursos(request):
    return HttpResponse("Vista de los cursos")
def entregable(request):
    return HttpResponse("Vista de los entregables")