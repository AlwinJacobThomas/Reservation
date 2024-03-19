from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)

class Booking(models.Model):
    name = models.CharField(max_length=50)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
class MenuTable(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    

    