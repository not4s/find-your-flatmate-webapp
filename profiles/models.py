from socket import INADDR_UNSPEC_GROUP
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='default_profile.jpeg')
    location = models.CharField(max_length=100, blank=True)
    studies_at = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
