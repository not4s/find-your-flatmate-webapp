from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    preference = models.CharField(max_length=200)