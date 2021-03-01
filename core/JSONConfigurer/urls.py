from django.contrib import admin
from django.urls import path, include

from django.views.decorators.csrf import csrf_exempt

from JSONConfigurer import views as views

app_name = "JSONConfigurer"
urlpatterns = [
  path('', views.home, name="home"),

  # Camera URLS
  path('listCamera',        views.listCamera,       name="list-camera"),
  path('camera',            views.createCamera,     name="create-camera"),
  path('camera/<int:id>',   views.camera,           name="camera"),

  # Mission URLS
  path('listMission',       views.listMission,      name="list-mission"),
  path('mission',           views.createMission,    name="create-mission"),
  path('mission/<int:id>',  views.mission,          name="mission"),
]
