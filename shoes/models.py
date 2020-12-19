from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from cloudinary.models import CloudinaryField


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(blank=False, max_length=20)

    def __str__(self):
        return self.brand_name


class Size(models.Model):
    SHOE_SIZES = (
        ('5', '5'),
        ('5.5', '5.5'),
        ('6', '6'),
        ('6.5', '6.5'),
        ('7', '7'),
        ('7.5', '7.5'),
        ('8', '8'),
        ('8.5', '8.5'),
        ('9', '9'),
        ('9.5', '9.5'),
        ('10', '10'),
        ('10.5', '10.5'),
        ('11', '11'),
    )

    sizes = MultiSelectField(choices=SHOE_SIZES)

    def __str__(self):
        return self.sizes


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
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    sizes = models.ForeignKey(Size, on_delete=models.CASCADE)
    shoeAvail = models.ForeignKey(Stock, on_delete=models.CASCADE)
    image = CloudinaryField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.shoeModel


class NewShoe(models.Model):
    shoeModel = models.CharField(blank=False, max_length=255)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    releaseDate = models.DateTimeField(default=datetime.now, blank=True)
    shoeAvail = models.ForeignKey(Stock, on_delete=models.CASCADE)
    sizes = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.shoeModel
