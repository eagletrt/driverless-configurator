from django.shortcuts import render

from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse

from .models import *
from .forms  import *


# Create your views here.
def home(req):

    return render(req, 'DashboardHome.html', {})
