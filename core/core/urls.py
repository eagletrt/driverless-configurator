from django.contrib import admin
from django.urls import path

from core.views import home

urlpatterns = [
    ## (Path, view function, pathName)
    path('', home, name="core-home"),
    path('admin/', admin.site.urls),
]
