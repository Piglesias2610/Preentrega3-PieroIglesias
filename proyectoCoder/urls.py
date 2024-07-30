
from django.contrib import admin
from django.urls import path,include
from appcoder.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("appcoder.urls"))
   
 ]