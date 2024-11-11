# Generated by Django 5.1.2 on 2024-11-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0004_alter_travel_duration_alter_travel_max_capacity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=10)),
                ('travels', models.ManyToManyField(blank=True, related_name='passengers', to='travels.travel')),
            ],
        ),
    ]
