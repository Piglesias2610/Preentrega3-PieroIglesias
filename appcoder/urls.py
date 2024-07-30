from django.urls import path
from appcoder.views import*

urlpatterns=[   
 
    path ('', inicio,name="inicio"),
    path('pagina-estudiantes', estudiante,name="estudiantes"),
    path('pagina-profesores',profesor,name="profes"),
    path('pagina-curso',cursos, name="cursos"),
    path('pagina-entregable', entregable,name="entregables")
 ]



 