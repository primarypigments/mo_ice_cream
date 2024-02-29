from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservations')
    phone_number = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time_slot = models.CharField(max_length=10, choices=[
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    ], null=False, blank=False)
    location = models.CharField(max_length=25, choices=[
        ('Kakenstorf', 'Kakenstorf'),
        ('Regesbostel', 'Regesbostel'),
        ('Brackel', 'Brackel'),
        ('Regesbostel', 'Brackel'),
        ('Wistedt', 'Wistedt'),
        ('Eyendorf', 'Eyendorf'),
    ], null=False, blank=False)
    status = models.CharField(max_length=10, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Canceled', 'Canceled'),
    ], default="Pending")
    book_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date
