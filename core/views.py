from django.shortcuts import render

def home(req):
  return render(req, 'core_home.html', {})