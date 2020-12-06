from django.db import models


# Create your models here.
class Shoe(models.Model):
    brand = models.CharField(blank=False, max_length=255)
    price = models.IntegerField(blank=False)
    color = models.CharField(blank=False, max_length=155)
    size = models.IntegerField(blank=False)

    def __str__(self):
        return self.brand + "" + str(self.price) + self.color + str(self.size)
