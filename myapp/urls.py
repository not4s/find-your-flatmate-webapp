from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r'^accepted/', views.accepted),
    path('', views.homepage),
]