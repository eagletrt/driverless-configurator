from ..models import CameraModel

import yaml
import json
from django.core import serializers

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