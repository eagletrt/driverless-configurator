from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect

from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms  import *

from .scripts.parser import *
from .scripts.load   import *

def home(req):
  return render(req, 'JSONHome.html', {})

#---------------------------------------------------#
## Login-Register
#---------------------------------------------------#

def loginPage(req):
  if req.user.is_authenticated:
    return redirect("JSONConfigurer:home")

  if req.method == "POST":
    username = req.POST.get("username")
    password = req.POST.get("password")

    user = authenticate(req, username=username, password=password)

    if not user == None:
      login(req, user)
      return redirect("JSONConfigurer:home")
    else:
      messages.info(req, "Username or password incorrect")

  context = {}
  return render(req, "user/login.html", context)

def registerPage(req):
  if req.user.is_authenticated:
    return redirect("JSONConfigurer:home")

  form  = UserForm(req.POST or None)

  if form.is_valid():
    form.save()
    return redirect('JSONConfigurer:login')

  context = {"form": form}
  return render(req, "user/register.html", context)

def logoutPage(req):
  logout(req)

  return redirect('JSONConfigurer:login')


#---------------------------------------------------#
## Camera
#---------------------------------------------------#

# List of all camera
# Allow to select and then edit
def listCamera(req):

  camera = CameraModel.objects.all()

  context = {
    "data": camera
  }

  return render(req, 'camera/listCamera.html', context)

# Blank form to be filled and saved
@login_required(login_url="JSONConfigurer:login")
def createCamera(req):

  mCamera = CameraForm(req.POST or None)

  if mCamera.is_valid():
    mCamera.save()

  context = {
    "camera": mCamera
  }
  return render(req, 'camera/camera.html', context)

# Detail of a camera
# Allow to edit delete or download camera
@login_required(login_url="JSONConfigurer:login")
def camera(req, id):
  camera = get_object_or_404(CameraModel, pk=id)

  mCamera = CameraForm(req.POST or None, instance=camera)

  keys = req.POST

  # Download button in camera.html
  if keys.get("download") == "Download":
    # Generating the yaml and saving it to a temp file
    filename = convertCameraToYaml(camera)

    # Downloading the file
    response = HttpResponse(open(filename, 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response

  # Save button in camera.html
  elif keys.get("submit") == "Save":
    if mCamera.is_valid():
      mCamera.save()
      return redirect("JSONConfigurer:list-camera")

  # Delete button in camera.html
  # Rendering the confirmation page
  elif keys.get("submit") == "Delete":
    return render(req, 'delete.html', {})

  # Delete button in delete.html (confirmation Page)
  elif keys.get("delete") == "Yes":
    camera.delete()
    return redirect("JSONConfigurer:list-camera", permanent=True)
  # Delete button in delete.html (confirmation Page)
  elif keys.get("delete") == "No":
    mCamera = CameraForm(None, instance=camera)

  context = {
    "camera": mCamera
  }
  return render(req, 'camera/camera.html', context)


#---------------------------------------------------#
## Mission
#---------------------------------------------------#

# List of all missions in DB
# Allow to enter in detail of the selected one
def listMission(req):

  missions = MissionModel.objects.all()

  context = {
    "data": missions
  }

  return render(req, 'mission/listMission.html', context)


# Blank Mission to be filled and saved
@login_required(login_url="JSONConfigurer:login")
def createMission(req):

  mMission = MissionForm(req.POST or None)

  if mMission.is_valid():
    mMission.save()

  context = {
    "mission": mMission
  }

  return render(req, 'mission/mission.html', context)

# Detail of a mission
# Allow to edit delete or download mission
@login_required(login_url="JSONConfigurer:login")
def mission(req, id):
  mission = get_object_or_404(MissionModel, id=id)

  mMission = MissionForm(req.POST or None, instance=mission)

  keys = req.POST
  # Download button in mission.html
  if keys.get("download") == "Download":
    # Converting all the model to JSON
    filename = convertMissionToJson(mission)
    # Dowloading the file
    response = HttpResponse(open(filename, 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response

  # Save button in mission.html
  elif keys.get("submit") == "Save":
    if mMission.is_valid():
      # Saving/Updatind mission
      mMission.save()
      return redirect("JSONConfigurer:list-mission")

  # Delete button in mission.html
  elif keys.get("submit") == "Delete":
    return render(req, 'delete.html', {})

  # Delete confirmation button in delete.html
  elif keys.get("delete") == "Yes":
    mission.delete()
    return redirect("JSONConfigurer:list-mission", permanent=True)

  # Delete confirmation button in delete.html
  elif keys.get("delete") == "No":
    # Resetting the form to the existing instance
    mMission = MissionForm(None, instance=mission)

  context = {
    "mission": mMission
  }

  return render(req, 'mission/mission.html', context)


#---------------------------------------------------#
## Slam
#---------------------------------------------------#

#---------------------------------------------------#
## ORB
#---------------------------------------------------#

#---------------------------------------------------#
## Viewer
#---------------------------------------------------#

#---------------------------------------------------#
## General Configuration
#---------------------------------------------------#
def listConfigurations(req):
    configurations = GeneralModel.objects.all()

    context = {
      "data": configurations
    }
    return render(req, "configuration/listConfiguration.html", context)

@login_required(login_url="JSONConfigurer:login")
def createConfiguration(req):
  mGeneral = GeneralForm(req.POST or None)

  if mGeneral.is_valid():
    mGeneral.save()

  context = {
    "configuration": mGeneral
  }
  return render(req, "configuration/configuration.html", context)

@login_required(login_url="JSONConfigurer:login")
def configuration(req, id):

  configuration = get_object_or_404(GeneralModel, id=id)

  mConfiguration = GeneralForm(req.POST or None, instance=configuration)

  keys = req.POST
  # Download button in mission.html
  if keys.get("download") == "Download":
    # Converting all the model to JSON
    filename = convertGeneralToJson(configuration)
    # Dowloading the file
    response = HttpResponse(open(filename, 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response

  # Save button in mission.html
  elif keys.get("submit") == "Save":
    if mConfiguration.is_valid():
      # Saving/Updatind mission
      mConfiguration.save()
      return redirect("JSONConfigurer:list-configuration")

  # Delete button in mission.html
  elif keys.get("submit") == "Delete":
    return render(req, 'delete.html', {})

  # Delete confirmation button in delete.html
  elif keys.get("delete") == "Yes":
    configuration.delete()
    return redirect("JSONConfigurer:list-confirmation", permanent=True)

  # Delete confirmation button in delete.html
  elif keys.get("delete") == "No":
    # Resetting the form to the existing instance
    mMission = GeneralForm(None, instance=configuration)

  context = {
    "configuration": mConfiguration
  }

  return render(req, "configuration/configuration.html", context)


#---------------------------------------------------#
## Load Configurations From File
#---------------------------------------------------#
def loadMissionFromFile(req):
    if req.method == "POST":
        mFile = req.FILES.get("file")
        if loadMission(mFile):
            return redirect("JSONConfigurer:list-mission")

    context = {}
    return render(req, "load.html", context)

def loadGeneralFromFile(req):
    if req.method == "POST":
        mFile = req.FILES.get("file")
        if loadGeneral(mFile):
            return redirect("JSONConfigurer:list-configuration")

    context = {}
    return render(req, "load.html", context)
