from django.contrib import admin
from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
]