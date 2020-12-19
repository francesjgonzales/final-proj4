from django.db import models

# Create your models here.


class Review(models.Model):
    starRating = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.starRating
