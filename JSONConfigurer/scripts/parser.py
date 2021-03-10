from ..models import *

import yaml
import json
from django.core import serializers

def convertMissionToJson(mission):

  j_m = serializers.serialize('json', [mission,])

  # Creating the mission JSON
  # But Foreign keys are shown only with pk
  data = json.loads(j_m)[0]["fields"]

  # Creating also the JSON of mission.camera (ForeignKey)
  camera = serializers.serialize('json', [mission.Camera,])
  cameraData = json.loads(camera)[0]["fields"]

  # Replacing the pk with the camera JSON
  data["Camera"] = cameraData

  data = json.dumps(data, indent=4)

  filename = "mission_configuration.json"
  nf = open(filename, "w")
  nf.write(data)
  nf.close()

  return filename

def convertCameraToYaml(camera):
  serialized = serializers.serialize('yaml', [camera,])

  dct = yaml.load(serialized, Loader=yaml.FullLoader)[0]["fields"]
  newDict = {}
  for key, val in dct.items():
    newKey = "Camera." + key
    newDict[newKey] = val

  filename = camera.name + ".yaml"
  nf = open(filename, "w")
  yaml.dump(newDict, nf, default_flow_style=False, sort_keys=False)
  nf.close()

  return filename

def convertGeneralToJson(configuration):

  serialized = serializers.serialize('json', [configuration,])

  # Creating the mission JSON
  # But Foreign keys are shown only with pk
  data = json.loads(serialized)[0]["fields"]

  # Creating also the JSON of mission.camera (ForeignKey)
  pk = serializers.serialize('json', [configuration.Camera,])
  cameraData = json.loads(pk)[0]["fields"]

  # Replacing the pk with the camera JSON
  data["Camera"] = cameraData

  pk = serializers.serialize('json', [configuration.SLAM,])
  slamData = json.loads(pk)[0]["fields"]
  data["SLAM"] = slamData

  pk = serializers.serialize('json', [configuration.ORBExtractor,])
  orbData = json.loads(pk)[0]["fields"]
  data["ORBExtractor"] = orbData

  pk = serializers.serialize('json', [configuration.Viewer,])
  viewerData = json.loads(pk)[0]["fields"]
  data["Viewer"] = viewerData

  data = json.dumps(data, indent=4)

  filename = "camera_configuration.json"
  nf = open(filename, "w")
  nf.write(data)
  nf.close()

  return filename
