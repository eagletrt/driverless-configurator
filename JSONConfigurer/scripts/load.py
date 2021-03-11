from ..models import *
from ..forms  import *

import yaml
import json
from django.core import serializers

def checkExistance(instance, Model):
    i_d = instance.__dict__
    del i_d["_state"]
    del i_d["id"]

    pk = -1
    for o in Model.objects.all():
        o_d = o.__dict__
        id = o_d["id"]
        del o_d["_state"]
        del o_d["id"]

        if(o_d == i_d):
            pk = id
            break
    return pk

def loadMission(filename):
    text = filename.read()
    j_s = json.loads(text)

    # Create form instance, it fills all the fields
    form = CameraForm(j_s["Camera"])

    if not form.is_valid():
        return

    # Create a model instance without saving in database
    instance = form.save(commit=False)
    # Check if the object exists in the database
    objPK = checkExistance(instance, CameraModel)

    if objPK > 0:
        # Beacuse Camera field if a ForeignKey is necessary to replace
        # this value with the primary key of the Camera object in the database
        j_s["Camera"] = objPK
    else:
        # If the camera is not in the database, save one and update the primarykey
        form = CameraForm(j_s["Camera"])
        instance = form.save()
        j_s["Camera"] = instance.id


    # Create Form
    form = MissionForm(j_s)
    if not form.is_valid():
        return

    # Check existance, and if it exists do nothing
    instance = form.save(commit=False)
    objPK = checkExistance(instance, MissionModel)

    if objPK > 0:
        print("Already exists")
    else:
        form = MissionForm(j_s)
        form.save()

    return 1


def loadGeneral(filename):
    text = filename.read()
    j_s = json.loads(text)

    print(j_s)


    '''
    #
    #   Camera
    #
    '''
    # Create form instance, it fills all the fields
    form = CameraForm(j_s["Camera"])
    if not form.is_valid():
        return
    # Create a model instance without saving in database
    instance = form.save(commit=False)
    # Check if the object exists in the database
    objPK = checkExistance(instance, CameraModel)

    if objPK > 0:
        # Beacuse Camera field if a ForeignKey is necessary to replace
        # this value with the primary key of the Camera object in the database
        j_s["Camera"] = objPK
    else:
        # If the camera is not in the database, save one and update the primarykey
        form = CameraForm(j_s["Camera"])
        instance = form.save()
        j_s["Camera"] = instance.id

    '''
    #
    #   SLAM
    #
    '''
    # Create form instance, it fills all the fields
    form = SLAMForm(j_s["SLAM"])
    if not form.is_valid():
        return
    # Create a model instance without saving in database
    instance = form.save(commit=False)
    # Check if the object exists in the database
    objPK = checkExistance(instance, SlamModel)

    if objPK > 0:
        # Beacuse Camera field if a ForeignKey is necessary to replace
        # this value with the primary key of the Camera object in the database
        j_s["SLAM"] = objPK
    else:
        # If the camera is not in the database, save one and update the primarykey
        form = SLAMForm(j_s["SLAM"])
        instance = form.save()
        j_s["SLAM"] = instance.id

    '''
    #
    #   ORBExtractor
    #
    '''
    # Create form instance, it fills all the fields
    form = ORBExtractorForm(j_s["ORBExtractor"])
    if not form.is_valid():
        return
    # Create a model instance without saving in database
    instance = form.save(commit=False)
    # Check if the object exists in the database
    objPK = checkExistance(instance, ORBExtractorModel)

    if objPK > 0:
        # Beacuse Camera field if a ForeignKey is necessary to replace
        # this value with the primary key of the Camera object in the database
        j_s["ORBExtractor"] = objPK
    else:
        # If the camera is not in the database, save one and update the primarykey
        form = ORBExtractorForm(j_s["ORBExtractor"])
        instance = form.save()
        j_s["ORBExtractor"] = instance.id

    '''
    #
    #   Viewer
    #
    '''
    # Create form instance, it fills all the fields
    form = ViewerForm(j_s["Viewer"])
    if not form.is_valid():
        return
    # Create a model instance without saving in database
    instance = form.save(commit=False)
    # Check if the object exists in the database
    objPK = checkExistance(instance, ViewerModel)

    if objPK > 0:
        # Beacuse Camera field if a ForeignKey is necessary to replace
        # this value with the primary key of the Camera object in the database
        j_s["Viewer"] = objPK
    else:
        # If the camera is not in the database, save one and update the primarykey
        form = ViewerForm(j_s["Viewer"])
        instance = form.save()
        j_s["Viewer"] = instance.id


    # Create Form
    form = GeneralForm(j_s)
    if not form.is_valid():
        return

    # Check existance, and if it exists do nothing
    instance = form.save(commit=False)
    objPK = checkExistance(instance, GeneralModel)

    if objPK > 0:
        print("Already exists")
    else:
        form = GeneralForm(j_s)
        form.save()

    return 1
