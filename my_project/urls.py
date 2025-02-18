"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from our hello_world app, import the views module, with the alias index_views
from hello_world import views as index_views
from about import views as about_views

urlpatterns = [
    path('', index_views.index, name='index'),      #call index method from our hello_world/views.py file
    path('about/', about_views.about, name='about'), #call about method from our about/views.py file
    path('admin/', admin.site.urls),
]
