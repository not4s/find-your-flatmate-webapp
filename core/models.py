from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Quiz(models.Model):
    sleep = models.IntegerField()
    cook  = models.IntegerField()
    loner = models.IntegerField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    quizDone = models.BooleanField(default=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Report(models.Model):
    username_to_report = models.CharField(max_length=100)
    details = models.TextField()