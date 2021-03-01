import os
from django.conf import settings
from django.db import models

from django.urls import reverse

missionOpts = [
    ("Acceleration", "Acceleration"),
    ("Trackdrive", "Trackdrive"),
    ("Skidpad", "Skidpad"),
    ("none", "none"),
  ]
  
defPath = os.path.dirname(os.path.abspath(__file__))

# Create your models here.
class CameraModel(models.Model):
  name = models.CharField(max_length=200)

  fx = models.FloatField()
  fy = models.FloatField()
  cx = models.FloatField()
  cy = models.FloatField()

  k1 = models.FloatField()
  k2 = models.FloatField()
  p1 = models.FloatField()
  p2 = models.FloatField()

  width   = models.IntegerField()
  height  = models.IntegerField()
  fps     = models.IntegerField()

  bf      = models.FloatField()
  BGR_RGB     = models.BooleanField(default=True)
  THDepth = models.IntegerField()

  def get_absolute_url(self):
    return reverse("JSONConfigurer:camera", kwargs={"id": self.id})

  def __str__(self):
    return "{}_{}_{}_{}".format(self.name, self.width, self.height, self.fps)

class MissionModel(models.Model):
  note = models.CharField(max_length=500, blank=True)

  mission = models.CharField(max_length=100, choices=missionOpts, default=missionOpts[0])

  mapping = models.BooleanField(default=True)

  rectsBeforeTracking = models.BooleanField(default=True)

  NNThreaded = models.BooleanField(default=True)
  PCLThreaded = models.BooleanField(default=True)

  datasetPath = models.CharField(max_length=300, default='/')

  camera = models.ForeignKey(
    CameraModel,
    on_delete=models.CASCADE,
    null=True,
    )

  def get_absolute_url(self):
    return reverse("JSONConfigurer:mission", kwargs={"id": self.id})