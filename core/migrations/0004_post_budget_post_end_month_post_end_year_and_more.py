# Generated by Django 4.0.5 on 2022-06-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_quiz_rename_report_content_report_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='budget',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='post',
            name='end_month',
            field=models.CharField(choices=[('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'), ('5', 'May'), ('6', 'Jun'), ('7', 'Jul'), ('8', 'Aug'), ('9', 'Sep'), ('10', 'Oct'), ('11', 'Nov'), ('12', 'Dec')], default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='end_year',
            field=models.CharField(choices=[('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027')], default=2022, max_length=4),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='start_month',
            field=models.CharField(choices=[('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'), ('5', 'May'), ('6', 'Jun'), ('7', 'Jul'), ('8', 'Aug'), ('9', 'Sep'), ('10', 'Oct'), ('11', 'Nov'), ('12', 'Dec')], default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='start_year',
            field=models.CharField(choices=[('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027')], default=2022, max_length=4),
        ),
    ]
