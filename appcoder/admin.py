from django.contrib import admin
from .models import *

class CursoAdmin(admin.ModelAdmin):
    list_display=("nombre","comision")
    list_filter=("nombre","comision")
    ordering=("nombre",)

class EstudianteAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","email")
    list_filter=("nombre","apellido","email")
    ordering=("nombre",)
# Register your models here.
admin.site.register(Curso,CursoAdmin)
admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Profesor)
admin.site.register(Entregable)