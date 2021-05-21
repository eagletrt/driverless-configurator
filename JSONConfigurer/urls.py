from django.contrib import admin
from django.urls import path, include

from django.views.decorators.csrf import csrf_exempt

from JSONConfigurer import views as views

app_name = "JSONConfigurer"
urlpatterns = [
  path('', views.home, name="home"),

  path('login/',                    views.loginPage,                name="login"),
  path('logout/',                   views.logoutPage,               name="logout"),
  path('register/',                 views.registerPage,             name="register"),

  # Camera URLS
  path('listCamera',                views.listCamera,               name="list-camera"),
  path('camera',                    views.createCamera,             name="create-camera"),
  path('camera/<int:id>',           views.camera,                   name="camera"),

  # Mission URLS
  path('listMission',               views.listMission,              name="list-mission"),
  path('mission',                   views.createMission,            name="create-mission"),
  path('mission/<int:id>',          views.mission,                  name="mission"),

  # General Configuration
  path('listConfigurations',       views.listConfigurations,        name="list-configuration"),
  path('configurations',           views.createConfiguration,       name="create-configuration"),
  path('configurations/<int:id>',  views.configuration,             name="configuration"),

  path('loadMission',               views.loadMissionFromFile,      name="load-mission"),
  path('loadGeneral',               views.loadGeneralFromFile,      name="load-general"),

  # # Slam URLS
  # path('listSlam',       views.listSlam,      name="list-slam"),
  # path('slam',           views.createSlam,     name="create-slam"),
  # path('slam/<int:id>',  views.slam,           name="slam"),
  #
  # # ORB URLS
  # path('listOrb',       views.listOrb,      name="list-orb"),
  # path('orb',           views.createOrb,     name="create-orb"),
  # path('orb/<int:id>',  views.orb,           name="orb"),
  #
  # # Viewer URLS
  # path('listViewer',       views.listViewer,      name="list-viewer"),
  # path('viewer',           views.createViewer,     name="create-viewer"),
  # path('viewer/<int:id>',  views.viewer,           name="viewer"),
]
