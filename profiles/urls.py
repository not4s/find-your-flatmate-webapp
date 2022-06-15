from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_page, name='profile_page'),
    path('settings', views.settings, name='settings'),
]
