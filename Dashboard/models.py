from django.db import models

# Create your models here.

class DataModel(models.Model):
    name = models.CharField(max_length=200)
    data = models.CharField(max_length=10485700)
