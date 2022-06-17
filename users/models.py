from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.jpeg', upload_to='profile_pics')
    about_me = models.TextField(blank=True, null=True)
    search_location = models.CharField(max_length=30, blank=True, null=True, choices=location_choice)
    studies_at = models.CharField(max_length=30, blank=True, null=True, choices=studies_at_choice)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)