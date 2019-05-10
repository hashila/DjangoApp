from django.contrib import admin
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.details,name='details'),
    url(r'^(?P<slug>[\w-]+)/$', views.fulldetails,name='fulldetails'),
]
