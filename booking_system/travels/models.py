from django.db import models

# Create your models here.

class Station(models.Model):
    code = models.CharField(max_length=3)
    town = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.town} ({self.code})"

class Travel(models.Model):
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
