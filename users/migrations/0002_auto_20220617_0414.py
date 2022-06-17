# Generated by Django 3.0.1 on 2022-06-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='search_location',
            field=models.CharField(blank=True, choices=[('Albertopolis', 'Albertopolis'), ('Bayswater', 'Bayswater'), ('Belgravia', 'Belgravia'), ('Brompton', 'Brompton'), ('Chelsea', 'Chelsea'), ('Chelsea Harbour', 'Chelsea Harbour'), ('Earls Court', 'Earls Court'), ('Holland Park', 'Holland Park'), ('Kensal Green', 'Kensal Green'), ('Kensington', 'Kensington'), ('Knightsbridge', 'Knightsbridge'), ('Ladbroke Grove', 'Ladbroke Grove'), ('North Kensington', 'North Kensington'), ('Notting Hill', 'Notting Hill'), ('South Kensington', 'South Kensington'), ('West Brompton', 'West Brompton'), ('West Kensington', 'West Kensington'), ('Worlds End', 'Worlds End')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='studies_at',
            field=models.CharField(blank=True, choices=[('English National Ballet School', 'English National Ballet School'), ('Royal College of Art', 'Royal College of Art'), ('Royal College of Music', 'Royal College of Music'), ('Imperial College London', 'Imperial College London'), ('Heythrop College', 'Heythrop College'), ('Richmond', 'Richmond'), ('Fordham University', 'Fordham University')], max_length=30, null=True),
        ),
    ]