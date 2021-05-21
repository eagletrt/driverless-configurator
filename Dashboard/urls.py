from django.urls import path, include

from django.views.decorators.csrf import csrf_exempt

from Dashboard import views as views

app_name = "Dashboard"
urlpatterns = [
  path('', views.home, name="home"),
]
