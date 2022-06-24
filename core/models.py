from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    location_choice = (
        ('Albertopolis', 'Albertopolis'),
        ('Bayswater', 'Bayswater'),
        ('Belgravia', 'Belgravia'),
        ('Brompton', 'Brompton'),
        ('Chelsea', 'Chelsea'),
        ('Chelsea Harbour', 'Chelsea Harbour'),
        ('Earls Court', 'Earls Court'),
        ('Holland Park', 'Holland Park'),
        ('Kensal Green', 'Kensal Green'),
        ('Kensington', 'Kensington'),
        ('Knightsbridge', 'Knightsbridge'),
        ('Ladbroke Grove', 'Ladbroke Grove'),
        ('North Kensington', 'North Kensington'),
        ('Notting Hill', 'Notting Hill'),
        ('South Kensington', 'South Kensington'),
        ('West Brompton', 'West Brompton'),
        ('West Kensington', 'West Kensington'),
        ('Worlds End', 'Worlds End'),
    )

    studies_at_choice = (
        ('English National Ballet School', 'English National Ballet School'),
        ('Royal College of Art', 'Royal College of Art'),
        ('Royal College of Music', 'Royal College of Music'),
        ('Imperial College London', 'Imperial College London'),
        ('Heythrop College', 'Heythrop College'),
        ('Richmond', 'Richmond'),
        ('Fordham University', 'Fordham University'),
    )

    budget_choice = (
        ('0-500', '0-500'),
        ('500-750', '500-750'),
        ('750-1000', '750-1000'),
        ('1000-1250', '1000-1250'),
        ('1250-1500', '1250-1500'),
        ('1500-1750', '1500-1750'),
        ('1750-2000', '1750-2000'),
        ('2000-3000', '2000-3000'),
        ('3000+', '3000+')
    )

    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    search_location = models.CharField(max_length=30, blank=True, null=True, choices=location_choice)
    studies_at = models.CharField(max_length=30, blank=True, null=True, choices=studies_at_choice)
    budget = models.CharField(max_length=30, blank=True, null=True, choices=budget_choice)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Report(models.Model):
    username_to_report = models.CharField(max_length=100)
    details = models.TextField()