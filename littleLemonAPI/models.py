from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateField()
    no_of_guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} -{self.no_of_guests} on {self.booking_date} "


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(10000)])
    inventory = models.PositiveIntegerField()
