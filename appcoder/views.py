from django.shortcuts import render
from appcoder.models import *

from django.shortcuts import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"appcoder/inicio.html")
def estudiante(request):
    return ("Vista de estudiantes")



def cursos(request):
    if request.method == 'POST':
        curso = Curso(nombre=request.POST['curso'], comision=request.POST['comision'])
        curso.save()
        return render(request, "appcoder/inicio.html")
    return render(request,"appcoder/curso_formulario.html")

def entregable(request):
    return HttpResponse("Vista de los entregables")



def profesor(request):
   if request.method == 'POST':
        profesor=Profesor(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'],profesion=request.POST['profesion'])
        profesor.save()
        return render(request, "appcoder/inicio.html")
   return render(request,"appcoder/profesor.html")
    
   
 
