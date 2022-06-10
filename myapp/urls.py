from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
=======
    path('accepted/', views.accepted),
>>>>>>> Stashed changes
    path('', views.homepage),
]