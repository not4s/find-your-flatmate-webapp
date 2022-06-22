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

    MONTHS = (
        ('1', 'Jan'),
        ('2', 'Feb'),
        ('3', 'Mar'),
        ('4', 'Apr'),
        ('5', 'May'),
        ('6', 'Jun'),
        ('7', 'Jul'),
        ('8', 'Aug'),
        ('9', 'Sep'),
        ('10', 'Oct'),
        ('11', 'Nov'),
        ('12', 'Dec'),
    )
    YEARS = (
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
    )
    start_month = models.CharField(max_length=2, choices=MONTHS, default=1)
    start_year = models.CharField(max_length=4, choices=YEARS, default=2022)
    end_month = models.CharField(max_length=2, choices=MONTHS, default=1)
    end_year = models.CharField(max_length=4, choices=YEARS, default=2022)
    location = models.CharField(max_length=20, default="")
    budget = models.IntegerField(max_length=3, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Report(models.Model):
    username_to_report = models.CharField(max_length=100)
    details = models.TextField()