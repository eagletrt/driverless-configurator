from django.contrib import admin

from .models import CameraModel, MissionModel

admin.site.register(CameraModel)
admin.site.register(MissionModel)