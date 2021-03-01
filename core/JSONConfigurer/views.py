from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect

from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse

from .models import CameraModel, MissionModel
from .forms  import CameraForm, MissionForm

from .scripts.cameraToYaml import *
from .scripts.missionToJson import *

def home(req):

  return render(req, 'JSONHome.html', {})



# List of all camera
# Allow to select and then edit
def listCamera(req):

  camera = CameraModel.objects.all()

  context = {
    "data": camera
  }

  return render(req, 'camera/listCamera.html', context)

# Blank form to be filled and saved
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


# List of all missions in DB
# Allow to enter in detail of the selected one
def listMission(req):

  missions = MissionModel.objects.all()

  context = {
    "data": missions  
  }

  return render(req, 'mission/listMission.html', context)


# Blank Mission to be filled and saved
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