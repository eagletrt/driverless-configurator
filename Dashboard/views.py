from django.shortcuts import render

from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse

from .models import *
from .forms  import *

import json

# Create your views here.
def home(req):

    return render(req, 'DashboardHome.html', {})

def set_data(req):

    if(req.method == "POST"):
        dd = json.loads(req.body)
        dd["object"] = str(dd["object"])
        dd["object"] = dd["object"].replace("\'", "\"")
        df = DataForm({"name":"mklvmdf", "data": dd["object"]})
        if(df.is_valid()):
            df.save()

    return JsonResponse("{}", safe=False)

def get_data(req):
    if(req.method == "GET"):
        datas = DataModel.objects.all()
        for data in datas:
            print(data.data)
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
