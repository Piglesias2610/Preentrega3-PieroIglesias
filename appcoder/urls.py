from django.urls import path
from appcoder.views import*

urlpatterns=[   path('', inicio),
    path('pagina-estudiantes', estudiante),
    path('pagina-profesores',profesor),
    path('pagina-curso', cursos),
    path('pagina-entregable', entregable)
 ]



