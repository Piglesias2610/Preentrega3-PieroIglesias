from django.urls import path
from appcoder.views import*

urlpatterns=[   
 
    path ('', inicio,name="inicio"),
    path('estudiante-formulario', estudiante,name="estudiantes"),
    path('profesor-formulario',profesor,name="profes"),
    path('curso-formulario',cursos, name="cursos"),
    path('entregable',agregar_entregable,name="entregables")
    
    
    
]
 



 