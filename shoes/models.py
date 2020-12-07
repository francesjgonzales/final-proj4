from django.db import models


# Create your models here.
class Shoe(models.Model):
    SHOE_AVAILABILITY = (
        ('Available', 'Available'),
        ('Sold-out', 'Sold Out')
    )

    CATEGORIES = (
        ('New-Release', 'NEW RELEASE'),
        ('Popular', 'POPULAR')
    )

    brand = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    size = models.DecimalField(max_digits=5, decimal_places=1)
    shoeAvail = models.CharField(max_length=9, choices=SHOE_AVAILABILITY)
    shoeCategories = models.CharField(max_length=11, choices=CATEGORIES)

    def __str__(self):
        return self.brand + "" + str(self.price) + self.color
        + str(self.size) + str(self.shoeAvail) + str(self.shoeCategories)
