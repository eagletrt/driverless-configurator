from django.urls import path, include

from django.views.decorators.csrf import csrf_exempt

from Dashboard import views as views

app_name = "Dashboard"
urlpatterns = [
  path('', views.home, name="home"),

  path('getData',             views.get_data, name="get-data"),
  path('setData', csrf_exempt(views.set_data), name="set-data"),
]
