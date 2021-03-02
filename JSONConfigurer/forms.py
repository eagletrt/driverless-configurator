from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm

from django.utils.timezone import now
# Create your models here.

from .models import CameraModel, MissionModel


class CameraForm(forms.ModelForm):
    class Meta():
        model = CameraModel
        fields = [
            "name",
            "fx",
            "fy",
            "cx",
            "cy",
            "k1",
            "k2",
            "p1",
            "p2",
            "width",
            "height",
            "fps",
            "bf",
            "BGR_RGB",
            "THDepth"
        ]

class MissionForm(forms.ModelForm):
    class Meta():
        model = MissionModel
        fields = [
            "note",
            "mission",
            "mapping",
            "rectsBeforeTracking",
            "NNThreaded",
            "PCLThreaded",
            "datasetPath",
            "camera",
        ]

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]