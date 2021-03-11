from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm

from django.utils.timezone import now
# Create your models here.

from .models import *


class CameraForm(forms.ModelForm):
    class Meta():
        model = CameraModel
        fields = "__all__"

class MissionForm(forms.ModelForm):
    class Meta():
        model = MissionModel
        fields = "__all__"

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]

class GeneralForm(forms.ModelForm):
    class Meta():
        model = GeneralModel
        fields = "__all__"

class SLAMForm(forms.ModelForm):
    class Meta():
        model = SlamModel
        fields = "__all__"

class ORBExtractorForm(forms.ModelForm):
    class Meta():
        model = ORBExtractorModel
        fields = "__all__"

class ViewerForm(forms.ModelForm):
    class Meta():
        model = ViewerModel
        fields = "__all__"
