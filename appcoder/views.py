from django.shortcuts import render
from appcoder.models import *
from appcoder.forms import *

from django.shortcuts import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,"appcoder/inicio.html")

def estudiante(request):
  if request.method == 'POST':
        estudiante=Estudiante(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'])
        estudiante.save()
        return render(request, "appcoder/inicio.html")
  return render(request,"appcoder/estudiante.html")
  
def cursos_create_api_form(request):
    if request.method == 'POST':
        miFormulario = curso_formulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], comision=informacion['comision' ])
            curso.save()
            return render(request,"appcoder/inicio.html")
    else:
        miFormulario = curso_formulario()
    return render(request, "appCoder/formulario_api.html", {"miFormulario": miFormulario})




def cursos(request):
    if request.method == 'POST':
        curso = Curso(nombre=request.POST['curso'], comision=request.POST['comision'])
        curso.save()
        return render(request, "appcoder/inicio.html")
    return render(request,"appcoder/curso_formulario.html")
def agregar_entregable(request):
    if request.method == 'POST':
        entregable=Entregable(nombre = request.POST['nombre'],fecha_entrega = request.POST['fecha_entrega'], entregado = request.POST.get('entregado') == 'on' )
       
        entregable.save()
        return render(request, "appcoder/inicio.html")  
    return render(request, "appcoder/entregables.html")  

def profesor(request):
   if request.method == 'POST':
        profesor=Profesor(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'],profesion=request.POST['profesion'])
        profesor.save()
        return render(request, "appcoder/inicio.html")
   return render(request,"appcoder/profesor.html")
    
def cursos_busqueda_api_form(request):
    if request.method == 'POST':
        miFormulario = BuscaCursoForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])
            return render(request, "appCoder/vercursos.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()
    return render(request, "appCoder/read_api_form.html", {"miFormulario": miFormulario})  
 
