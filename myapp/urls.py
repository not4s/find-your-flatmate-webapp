from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('accepted/', views.accepted),
=======
    path(r'^accepted/', views.accepted),
>>>>>>> jiaqi-AcceptedScreen
    path('', views.homepage),
]