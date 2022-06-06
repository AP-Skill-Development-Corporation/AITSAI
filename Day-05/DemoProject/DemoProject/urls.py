"""DemoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from SampleApp import views
from BootApp import views as ba
urlpatterns = [
    path('admin/', admin.site.urls),
    path('h/',views.sample),
    path('gt/<str:t>/',views.demo),
    path('v/<str:y>/<int:e>/',views.st),
    path('hw/<str:b>/',views.gt),
    path('q/<str:sd>/',views.hk),
    path('z/',views.cds),
    path('emp/<str:en>/<int:sal>/<int:ag>/',views.empdtls),
    path('emprg/',views.empregister),
    path('',ba.bth,name="hm"),
    path('rg/',ba.reg),
    path('u/',ba.dsg,name="rgt"),
    path('cr/',ba.crd,name="cd"),
    path('usup/<int:e>/',ba.usupd,name="up"),
    path('usd/<int:w>/',ba.usdt,name="dt"),
]
