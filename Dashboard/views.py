from django.shortcuts import render

from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse

from .models import *
from .forms  import *

import json

# Create your views here.
def home(req):

    return render(req, 'DashboardHome.html', {})


def get_data(req):


    if(req.method == "GET"):
        datas = DataModel.objects.all()
        for data in datas:
            print(data.data)
            d_j = json.loads(data.data)
            d_j = d_j[0]
            labels = []
            data = []
            for key in d_j.keys():
                for sub_key in d_j[key].keys():
                    labels.append(key + sub_key)
                    data.append([d_j[key][sub_key]])
            print(labels)
            print(data)
            return JsonResponse({"labels": labels, "data": data, "x": [0,0,0,0,0]})


    return JsonResponse("{}", safe=False)
