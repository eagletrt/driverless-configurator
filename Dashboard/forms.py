from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm

from django.utils.timezone import now
# Create your models here.

from .models import *

class DataForm(forms.ModelForm):
    class Meta():
        model = DataModel
        fields = "__all__"


class RealTimeForm(forms.ModelForm):
    class Meta():
        model = RealTimeModel
        fields = "__all__"
