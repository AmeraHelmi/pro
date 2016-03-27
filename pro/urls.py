"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import *
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^itemsearch/$',itemsearch),
    url(r'^sheksearch/$',sheksearch),
    url(r'^delipro/(?P<pid>\d+)',delipro),
    url(r'^usepro/(?P<pid>\d+)',usepro),
    url(r'^editpro/(?P<pid>\d+)',editpro),
     url(r'^projects/$',projects),
    url(r'^getproinfo/$',getproinfo),
    url(r'^search/$',search),
    url(r'^m2awelsearch/$',m2awelsearch),
    url(r'^start/$',start),
    url(r'^some_view/$',pdf_printer),
    url(r'^accounts/$',accounts),
    url(r'^m2alen/$',m2alen),
    url(r'^accountsbydate/$',accountsbydate),
    url(r'^shekat/$',shekat),
    url(r'^today/$',today),
    url(r'^register/$',register),
    url(r'^viewm2awel/(?P<uid>\d+)',viewm2awel),
    url(r'^login/$',login),
    url(r'^logout/$',logout),
    url(r'^additem/$',additem),
    url(r'^addm2awel/$',addm2awel),
    url(r'^addshek/$',addshek),
    url(r'^delitem/(?P<uid>\d+)',delitem),
    url(r'^addAction/(?P<uid>\d+)',addaction),
    url(r'^delshek/(?P<uid>\d+)',delshek),
    url(r'^delm2awel/(?P<uid>\d+)',delm2awel),
    url(r'^edititem/(?P<uid>\d+)',edititem),
    url(r'^editshek/(?P<uid>\d+)',editshek),
    url(r'^editm2awel/(?P<uid>\d+)',editm2awel),
    url(r'^edititem/(?P<uid>\w+)',search),
    url(r'^editaction/(?P<uid>\d+)/(?P<aid>\d+)',editaction),
    url(r'^report/$',report),
    url(r'^addpro/$',addpro),
    url(r'^addj/$',addproj),
    url(r'^sheksearch/$',sheksearch),
]
