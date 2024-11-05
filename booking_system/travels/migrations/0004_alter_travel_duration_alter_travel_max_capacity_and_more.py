# Generated by Django 5.1.2 on 2024-11-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0003_travel_departure_time_travel_driver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='duration',
            field=models.IntegerField(default=0, help_text='Duration of the journey in minutes'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='max_capacity',
            field=models.PositiveIntegerField(default=0, help_text='Maximum seating capacity of the vehicle'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='remaining_seats',
            field=models.PositiveIntegerField(default=0, help_text='Number of seats currently available'),
        ),
    ]