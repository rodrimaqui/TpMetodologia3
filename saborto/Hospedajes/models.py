from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Guest(models.Model):
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    code = models.CharField(max_length=50)
    total = models.IntegerField()

    def __str__(self):
        return self.code

class Property(models.Model):
    description = models.CharField(max_length=500)
    priceDays = models.IntegerField()
    image = models.CharField(max_length=70)
    title = models.CharField(max_length=50)
    numberCard = models.IntegerField()
    maxGuest = models.IntegerField()
    city = models.ForeignKey(City)
    reservation = models.ForeignKey(Reservation)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title
class DateRental(models.Model):
    date = models.DateField()
    property = models.ForeignKey(Property)
    reservation = models.ForeignKey(Reservation)

    def __str__(self):
        return self.date
