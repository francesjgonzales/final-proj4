from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(blank=False, max_length=20)

    def __str__(self):
        return self.brand_name


class Stock(models.Model):
    SHOE_AVAILABILITY = (
        ('In-stock', 'In Stock'),
        ('Sold-out', 'Sold Out'),
        ('Upcoming', 'Upcoming')
    )

    shoeAvail = models.CharField(max_length=9, choices=SHOE_AVAILABILITY)

    def __str__(self):
        return self.shoeAvail


class Tag(models.Model):
    shoeModel = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.shoeModel


class Shoe(models.Model):
    shoeModel = models.CharField(blank=False, max_length=255)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    shoe_size = models.CharField(blank=False, max_length=50)
    color = models.CharField(blank=False, max_length=155)
    shoeAvail = models.ForeignKey(Stock, on_delete=models.CASCADE)
    releaseDate = models.CharField(max_length=80, blank=True)
    image = CloudinaryField()
    tags = models.ManyToManyField(Tag)
    adminUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    shoeQty = models.DecimalField(blank=False, max_digits=5, decimal_places=0)

    def __str__(self):
        return self.shoeModel
