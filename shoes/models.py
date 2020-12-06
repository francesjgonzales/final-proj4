from django.db import models


# Create your models here.
class Shoe(models.Model):
    BOOL_OPTIONS = (
        (True, 'Available'),
        (False, 'Sold Out')
    )

    SHOE_AVAILABILITY = (
        ('available', 'Available'),
        ('sold-out', 'Sold Out')
    )

    brand = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    soldOut = models.BooleanField(choices=BOOL_OPTIONS)
    shoeAvail = models.CharField(max_length=9, choices=SHOE_AVAILABILITY)

    def __str__(self):
        return self.brand + "" + str(self.price) + self.color 
        + str(self.size) + str(self.soldOut) + str(self.shoeAvail)
