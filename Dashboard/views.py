from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse


from .models import *
from .forms  import *

import time

import json

# Create your views here.
def home(req):
    return render(req, 'DashboardHome.html', {})


def view(req, id):
    obj = get_object_or_404(DataModel, id=id)
    obj.data = json.loads(obj.data)
    context = {
        "names": obj.data.keys(),
        "data": json.dumps(obj.data),
    }
    return render(req, 'Dashboard.html', context)

def set_data(req):
    if(req.method == "POST"):
        dd = json.loads(req.body)
        dd["object"]["data"] = str(dd["object"]["data"])
        dd["object"]["data"] = dd["object"]["data"].replace("\'", "\"")
        df = DataForm({"name": dd["object"]["name"], "data": dd["object"]["data"]})
        if(df.is_valid()):
            df.save()

    return JsonResponse("{}", safe=False)

def get_data(req):
    if(req.method == "GET"):
        datas = DataModel.objects.all()
        for data in datas:
            d_j = json.loads(data.data)
            labels = []
            data = []
            max = 0
            for key in d_j.keys():
                for sub_key in d_j[key].keys():
                    labels.append(key + sub_key)
                    data.append([d_j[key][sub_key]])
                    if len([d_j[key][sub_key]][0]) > max:
                        max = len([d_j[key][sub_key]][0])

            x = []
            for i in range(0, max):
                x.append(i)
            return JsonResponse({"labels": labels, "data": data, "x": x})


    return JsonResponse("{}", safe=False)


def database(req):

    objs = DataModel.objects.all()

    context = {
        "data": objs
    }

    return render(req, "Database.html", context)


def real_time(req):

    obj = list(RealTimeModel.objects.all())[0]
    obj.data = json.loads(obj.data)
    context = {
        "realtime": True,
        "names": obj.data.keys(),
        "data": json.dumps(obj.data),
    }
    return render(req, "Dashboard.html", context)

def rt_get_data(req, sensor):
    sensor = sensor.replace("-", " ")
    obj = list(RealTimeModel.objects.all())[0]
    print(obj.timestamp)

    # data is string in json format, so load it
    d_j = json.loads(obj.data)
    d_j = d_j[str(sensor)]

    # setup labels and data arrays
    labels = []
    data = d_j

    # max count of elements to setup x axis
    max = 0
    for key in d_j.keys():
        labels.append(key)
        if len(d_j[key]) > max:
            max = len(d_j[key])
    print(labels)
    print(data)
    context = {
        "realtime": True,
        "names": [sensor],
        "data": json.dumps(d_j),
    }
    return JsonResponse(context, safe=False)

def rt_set_data(req):
    if(req.method == "POST"):
        dd = json.loads(req.body)
        dd["object"]["data"] = str(dd["object"]["data"])
        dd["object"]["data"] = dd["object"]["data"].replace("\'", "\"")
        df = RealTimeForm({"name": dd["object"]["name"], "data": dd["object"]["data"], "timestamp": str(time.time())})
        if(df.is_valid()):
            RealTimeModel.objects.all().delete()
            df.save()

    return JsonResponse("{}", safe=False)
