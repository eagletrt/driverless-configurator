from django.contrib import admin
from django.urls import path, include

from core.views import home

urlpatterns = [
    ## (Path, view function, pathName)
    path('', home, name="core-home"),
    path('admin/', admin.site.urls),

    # Including urlpatterns from JSONConfigurer app
    path("JSONConfigurer/", include("JSONConfigurer.urls"))
]