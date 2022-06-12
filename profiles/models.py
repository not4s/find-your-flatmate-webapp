from socket import INADDR_UNSPEC_GROUP
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = ''
    id_user = ''
    bio = ''
    profile_img = models.ImageField(upload_to='profile_images')
    location = ''