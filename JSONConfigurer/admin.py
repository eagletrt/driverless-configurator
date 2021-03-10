from django.contrib import admin

from .models import *

admin.site.register(CameraModel)
admin.site.register(MissionModel)
admin.site.register(SlamModel)
admin.site.register(ORBextractorModel)
admin.site.register(ViewerModel)
admin.site.register(GeneralModel)
