from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"appcoder/inicio.html")
def estudiante(request):
    return ("Vista de estudiantes")
def profesor(request):
    return HttpResponse("Vista de profesores")
def cursos(request):
    return render (request,"appcoder/cursos.html")
def entregable(request):
    return HttpResponse("Vista de los entregables")