import os
from django.conf import settings
from django.db import models
from django.db.models import *

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
  Note = models.CharField(max_length=500, blank=True)

  Mission = models.CharField(max_length=100, choices=missionOpts, default=missionOpts[0])

  Mapping = models.BooleanField(default=True)

  RectsBeforeTracking = models.BooleanField(default=True)

  NNThreaded = models.BooleanField(default=True)
  PCLThreaded = models.BooleanField(default=True)

  DatasetPath = models.CharField(max_length=300, default='/')

  Camera = models.ForeignKey(
    CameraModel,
    on_delete=models.CASCADE,
    null=True,
    )

  def get_absolute_url(self):
    return reverse("JSONConfigurer:mission", kwargs={"id": self.id})

class SlamModel(models.Model):
    RGB = BooleanField(default=True)
    ThDepth = IntegerField()
    DepthMapFactor = IntegerField()
    # def get_absolute_url(self):
    #   return reverse("JSONConfigurer:mission", kwargs={"id": self.id})
    def __str__(self):
        return "rgb:{},ThDepth:{},DepthMapFactor:{}".format(self.RGB, self.ThDepth, self.DepthMapFactor)

class ORBextractorModel(models.Model):
    nFeautures = IntegerField()
    scaleFactor = FloatField()
    nLevels = IntegerField()
    iniThFAST = IntegerField()
    minThFAST = IntegerField()
    # def get_absolute_url(self):
    #   return reverse("JSONConfigurer:mission", kwargs={"id": self.id})
    def __str__(self):
        return "nFeatures:{},scaleFactor:{},nLevels{}".format(self.nFeautures, self.scaleFactor, self.nLevels)

class ViewerModel(models.Model):
    KeyFrameSize = FloatField()
    KeyFrameLineWidth = FloatField()
    ReferenceSystemSize = FloatField()
    ReferenceSystemLineWidth = FloatField()
    GraphLineWidth = FloatField()
    PointSize = FloatField()
    CameraSize = FloatField()
    CameraLineWidth = FloatField()
    ViewpointX = FloatField()
    ViewpointY = FloatField()
    ViewpointZ = FloatField()
    ViewpointF = FloatField()

    def __str__(self):
        return "KFSize:{},KFLineWidth:{}".format(self.KeyFrameSize, self.KeyFrameLineWidth)

class GeneralModel(models.Model):
    note = CharField(max_length=500, blank=True)

    Camera = ForeignKey(
        CameraModel,
        on_delete=models.CASCADE,
        null=True
    )
    SLAM = ForeignKey(
        SlamModel,
        on_delete=models.CASCADE,
        null=True
    )
    ORBExtractor = ForeignKey(
        ORBextractorModel,
        on_delete=models.CASCADE,
        null=True
    )
    Viewer = ForeignKey(
        ViewerModel,
        on_delete=models.CASCADE,
        null=True
    )

    def get_absolute_url(self):
      return reverse("JSONConfigurer:configuration", kwargs={"id": self.id})

    def __str__(self):
        return "{}\r\nCamera: {}\r\nSlam: {}\r\nORB: {}\r\nViewer: {}".format(self.note, self.Camera, self.SLAM, self.ORBExtractor, self.Viewer)
