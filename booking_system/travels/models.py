from django.db import models
from django.utils import timezone

class Station(models.Model):
    code = models.CharField(max_length=3)
    town = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.town} ({self.code})"

class Travel(models.Model):
    VEHICLE_TYPES = [
        ('Bus', 'Bus'),
        ('Matatu', 'Matatu'),
    ]

    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField(help_text="Duration of the journey in minutes", default=60)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Price of the journey")
    number_plate = models.CharField(max_length=10, unique=True, null=True, blank=True, help_text="Vehicle number plate")
    vehicle_type = models.CharField(max_length=6, choices=VEHICLE_TYPES, default='Matatu', help_text="Type of vehicle (Bus or Matatu)")
    max_capacity = models.PositiveIntegerField(help_text="Maximum seating capacity of the vehicle", default=15)
    driver = models.CharField(max_length=64, help_text="Name of the driver", default="Driver Name")
    departure_time = models.DateTimeField(help_text="Departure date and time", default=timezone.now)
    remaining_seats = models.PositiveIntegerField(help_text="Number of seats currently available", default=15)

    def __str__(self):
        return f"{self.origin} to {self.destination} at {self.departure_time}"

    def save(self, *args, **kwargs):
        # Ensure remaining seats does not exceed max_capacity
        if self.remaining_seats > self.max_capacity:
            self.remaining_seats = self.max_capacity
        super().save(*args, **kwargs)
