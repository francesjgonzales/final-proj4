from django.contrib.auth.models import User
from django.db import models
from shoes.models import Shoe

# Create your models here.


class Purchase(models.Model):
    shoe_id = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    qty = models.IntegerField(blank=False)

    def __str__(self):
        return f"Purchase no {self.shoe.id} by user {self.user.id}"
