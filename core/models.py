from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class PostManager(models.Manager):
    def ordered_by_diff(self, request):
        qs = self.get_queryset()
        return sorted(qs, key=lambda x: post_difference(request, x))


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
        ('0-500', '£0-500'),
        ('500-750', '£500-750'),
        ('750-1000', '£750-1000'),
        ('1000-1250', '£1000-1250'),
        ('1250-1500', '£1250-1500'),
        ('1500-1750', '£1500-1750'),
        ('1750-2000', '£1750-2000'),
        ('2000-3000', '£2000-3000'),
        ('3000+', '£3000+')
    )
    sleep_choice = (
        (1, '21:00'),
        (2, '22:00'),
        (3, '23:00'),
        (4, '24:00+'),
    )

    cook_choice = (
        (1, '0'),
        (2, '1-2'),
        (3, '3-4'),
        (4, '5+'),
    )

    loner_choice = (
        (1, 'None'),
        (2, 'Once per week'),
        (3, '2-4 times per week'),
        (4, 'A lot'),
    )

    visit_choice = (
        (1, "Never"),  
        (2, "Around once a month"), 
        (3, "Once a week"), 
        (4, "More than once a week")
    )

    back_choice = (
        (1, "Afternoon"),  
        (2, "Evening"), 
        (3, "Late at night"), 
        (4, "Morning")
    )

    # shower_choice = (
    #     (1, "Morning"),
    #     (2, "Noon"),
    #     (3, "Evening"),
    #     (4, "Right before bed")
    # )

    groceries_choice = (
        (1, "Once per week"),
        (2, "2-3 times per week"),
        (3, "4-5 times per week"),
        (4, "Basically every day")
    )

    # alcohol_choice = (
    #     (1, "I don't drink"),
    #     (2, "1-2 times per week"),
    #     (3, "4-5 times per week"),
    #     (4, "Basically every day")
    # )
    
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    search_location = models.CharField(max_length=30, blank=True, null=True, choices=location_choice)
    studies_at = models.CharField(max_length=30, blank=True, null=True, choices=studies_at_choice)
    budget = models.CharField(max_length=30, blank=True, null=True, choices=budget_choice)

    what_time_do_you_go_to_sleep = models.IntegerField(choices=sleep_choice, blank=True, null=True)
    how_often_do_you_cook_per_week = models.IntegerField(choices=cook_choice, blank=True, null=True)
    how_often_do_you_meet_friends_per_week = models.IntegerField(choices=loner_choice, blank=True, null=True)
    how_often_do_you_have_guests = models.IntegerField(choices=visit_choice, blank=True, null=True)
    when_do_you_usually_return_to_the_flat = models.IntegerField(choices=back_choice, blank=True, null=True)
    # how_often_do_you_drink_alcohol = models.IntegerField(choices=alcohol_choice, blank=True, null=True)
    
    # when_do_you_shower = models.IntegerField(choices=shower_choice, blank=True, null=True)
    how_often_do_you_shop_for_groceries = models.IntegerField(choices=groceries_choice, blank=True, null=True)
    # how_often_do_you_do_chores = models.IntegerField(choices=groceries_choice, blank=True, null=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

def post_difference(request, post):
    difference = 0
    difference += abs(int(post.what_time_do_you_go_to_sleep) - int(request.POST['what_time_do_you_go_to_sleep']))
    difference += abs(int(post.how_often_do_you_cook_per_week) - int(request.POST['how_often_do_you_cook_per_week']))
    difference += abs(int(post.how_often_do_you_meet_friends_per_week) - int(request.POST['how_often_do_you_meet_friends_per_week']))
    difference += abs(int(post.how_often_do_you_have_guests) - int(request.POST['how_often_do_you_have_guests']))
    difference += abs(int(post.when_do_you_usually_return_to_the_flat) - int(request.POST['when_do_you_usually_return_to_the_flat']))
    difference += abs(int(post.how_often_do_you_shop_for_groceries) - int(request.POST['how_often_do_you_shop_for_groceries']))

    return difference

class Report(models.Model):
    username_to_report = models.CharField(max_length=100)
    details = models.TextField()