from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse


from .models import *
from .forms  import *

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


    return render(req, "Dashboard.html", {})
