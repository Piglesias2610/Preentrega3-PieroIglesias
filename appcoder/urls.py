from django.urls import path
from appcoder.views import*

urlpatterns=[   
 
    path ('', inicio,name="inicio"),
    path('pagina-estudiantes', estudiante,name="estudiantes"),
    path('profesor-formulario',profesor,name="profes"),
    path('curso-formulario',cursos, name="cursos"),
    path('pagina-entregable', entregable,name="entregables"),
    
    
]
 



 