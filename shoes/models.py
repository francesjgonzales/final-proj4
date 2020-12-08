from django.db import models
from datetime import date, datetime


# Create your models here.
class Shoe(models.Model):
    SHOE_AVAILABILITY = (
        ('In-stock', 'In Stock'),
        ('Sold-out', 'Sold Out'),
        ('Upcoming', 'Upcoming')
    )

    shoeModel = models.CharField(blank=False, max_length=255)
    shoeBrand = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    size = models.DecimalField(max_digits=5, decimal_places=1)
    shoeAvail = models.CharField(max_length=9, choices=SHOE_AVAILABILITY)

    def __str__(self):
        return self.shoeModel + "" + self.shoeBrand


class NewShoe(models.Model):
    SHOE_AVAILABILITY = (
        ('In-stock', 'In Stock'),
        ('Sold-out', 'Sold Out'),
        ('Coming-Soon', 'Coming Soon')
    )

    shoeModel = models.CharField(blank=False, max_length=255)
    shoeBrand = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    releaseDate = models.DateTimeField(default=datetime.now, blank=True)
    shoeAvail = models.CharField(max_length=11, choices=SHOE_AVAILABILITY)

    def __str__(self):
        return self.shoeModel
