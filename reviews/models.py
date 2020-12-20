from django.db import models
from shoes.models import Shoe
from django.contrib.auth.models import User


# Create your models here.


class Review(models.Model):
    BOOL_OPTIONS = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    starRating = models.CharField(blank=False, max_length=255)
    opinion = models.TextField(blank=False, max_length=100)
    details = models.TextField(blank=False, max_length=200)
    recommend = models.CharField(max_length=3, choices=BOOL_OPTIONS)
    adminUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.starRating
