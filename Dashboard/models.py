from django.db import models
from django.db.models.base import Model

from django.urls import reverse

# Create your models here.


class DataModel(models.Model):
    name = models.CharField(max_length=200)
    data = models.CharField(max_length=10485700)

    def get_absolute_url(self):
        return reverse("Dashboard:view", kwargs={"id": self.id})


class RealTimeModel(models.Model):
    name = models.CharField(max_length=200)
    data = models.CharField(max_length=10485700)
    timestamp = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("Dashboard:view", kwargs={"id": self.id})


class StringModel(models.Model):
    data = models.CharField(max_length=10485700)
