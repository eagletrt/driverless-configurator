from ..models import MissionModel

import json
from django.core import serializers

def convertMissionToJson(mission):
  j_m = serializers.serialize('json', [mission,])

  # Creating the mission JSON
  # But Foreign keys are shown only with pk
  data = json.loads(j_m)[0]["fields"]

  # Creating also the JSON of mission.camera (ForeignKey)
  camera = serializers.serialize('json', [mission.camera,])
  cameraData = json.loads(camera)[0]["fields"]

  # Replacing the pk with the camera JSON
  data["camera"] = cameraData

  data = json.dumps(data, indent=4)

  filename = "mission.json"
  nf = open(filename, "w")
  nf.write(data)
  nf.close()

  return filename

