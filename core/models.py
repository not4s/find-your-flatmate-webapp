from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# class Quiz(models.Model):
#     sleep_choice = (
#         (1, '21:00'),
#         (2, '22:00'),
#         (3, '23:00'),
#         (4, '24:00+'),
#     )

#     cook_choice = (
#         (1, '0'),
#         (2, '1-2'),
#         (3, '3-4'),
#         (4, '5+'),
#     )

#     loner_choice = (
#         (1, 'None'),
#         (2, 'Once per week'),
#         (3, '2-4 times per week'),
#         (4, 'A lot'),
#     )

#     sleep = models.IntegerField(choices=sleep_choice)
#     cook  = models.IntegerField(choices=cook_choice)
#     loner = models.IntegerField(choices=loner_choice)

#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={'pk': Post.objects.last().pk})

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # quizDone = models.BooleanField(default=False)
    # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)

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

    shower_choice = (
        (1, "Morning"),
        (2, "Noon"),
        (3, "Evening"),
        (4, "Right before bed")
    )

    groceries_choice = (
        (1, "Once per week"),
        (2, "2-3 times per week"),
        (3, "4-5 times per week"),
        (4, "Basically every day")
    )

    alcohol_choice = (
        (1, "I don't drink"),
        (2, "1-2 times per week"),
        (3, "4-5 times per week"),
        (4, "Basically every day")
    )

    what_time_do_you_go_to_sleep = models.IntegerField(choices=sleep_choice, blank=True, null=True)
    how_often_do_you_cook_per_week = models.IntegerField(choices=cook_choice, blank=True, null=True)
    how_often_do_you_meet_friends_per_week = models.IntegerField(choices=loner_choice, blank=True, null=True)
    how_often_do_you_think_you_will_bring_other_people_into_the_flat = models.IntegerField(choices=visit_choice, blank=True, null=True)
    when_do_you_usually_return_to_the_flat = models.IntegerField(choices=back_choice, blank=True, null=True)
    how_often_do_you_drink_alcohol = models.IntegerField(choices=alcohol_choice, blank=True, null=True)
    
    when_do_you_shower = models.IntegerField(choices=shower_choice, blank=True, null=True)
    how_often_do_you_shop_for_groceries = models.IntegerField(choices=groceries_choice, blank=True, null=True)
    how_often_do_you_do_chores = models.IntegerField(choices=groceries_choice, blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Report(models.Model):
    username_to_report = models.CharField(max_length=100)
    details = models.TextField()