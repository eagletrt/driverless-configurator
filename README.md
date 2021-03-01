# driverless-configurator
Online django configurator for driverless perception team.

## core
App for perception team to configure camera and mission by creating yaml and json file.

To start the app:
~~~bash
cd core
python3 manage.py runserver
~~~

This way the core app will start at local ip: 127.0.0.1:8000

## Requirements
Postgres database

## Create New Project
To create a new project make sure to install Django

~~~bash
pip3 install Django
~~~
### Create Project
Then to create a project called myProject run:
~~~bash
django-admin startproject myProject
~~~

Then the project is empty, navigate into it and run:
~~~bash
python3 manage.py runserver
~~~

A warning is shown, that is because django need a DB, so to create it run:
~~~bash
python3 manage.py makemigrations
python3 manage.py mirate
~~~

Now go to **127.0.0.1:8000**


### Create new app
All your pages will be developed on the app, not on the main project.  
The main Project is used only as a common start point of all the apps.  

So to create myapp run:
~~~bash
django-admin startapp myapp
~~~

The next step is to link the main project to myapp.

In myapp folder create a file **urls.py**.  
This file will implement all the routes of the myapp.  
The implementation of this file is similar to **myProject/urls.py**.


To effectively link myProject in **myProject/urls.py** add at the top:
~~~python
from django.urls import include
~~~
and then add a path:
~~~python
path("myapp/", include("myapp.urls"))
~~~

This last line means: "If the route is myapp then import the myapp.urls and take from there the url paths"  
In **myapp/urls.py** the routes are truncated, so if the route is *myapp/pages/1* will be catched from **myapp/urls.py** as *pages/1*

The project can't run rigth now, we need to implement **myapp/urls.py** and the html pages.

Now that we have the routes we need to implement basic html pages.  
So to organize the project create a folder named **teplates** in the root folder.  
Here will be added templates that can be viewed/used from all the apps.  
To create a page needed for only one app create a **teplates** folder in the app subdirectory.

To let django find the templates folder edit **myProject/settings.py** and edit:
~~~python
TEMPLATES = [
  {
    DIRS: [],
  }  
]
~~~
To
~~~python
TEMPLATES = [
  {
    DIRS: [BASE_DIR.joinpath("templates")],
  }  
]
~~~
And make sure that **APP_DIRS** is set to **True**

Now create a page named home.html and save it into **myapp/templates/**, implement as you like.

Then we want our project to render this new page on if the url **myapp/** is requested.  
To do that we need to implement a path and a function that render the page.  
The path is in **urls.py** and the page is implemented in **myapp/views.py**.  
Let's edit **urls.py**. Clear all the file and paste this code:
~~~python
from django.urls import path

from myapp import views as views  # import our views file that can return html page to be rendered

app_name = "myapp"
urlpatterns = [
  path('', views.home, name="home"),
]
~~~

So now the **urls.py** is looking for a funcion called **home** in **myapp/views.py** file.  
To implement that function copy the following code in **myapp/views.py**:
~~~python
from django.shortcuts import render

def home(request):
  return render(request, 'home.html', {})
~~~

This function is now taking a request as argument, looking for a template called home.html and passing an empty dict to that html page.  
The dict can be accessed from the html to the containing data.  
The dict is called **context**.

Now the app should be working, so to the url: *127.0.0.1:8000/myapp* showld be rendered *home.html* page.
Make sure that:
~~~bash
python3 manage.py runserver
~~~
Is running