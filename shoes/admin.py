from django.contrib import admin
from .models import Shoe, NewShoe, Brand, Stock, Tag

# Register your models here.
admin.site.register(Shoe)
admin.site.register(NewShoe)
admin.site.register(Brand)
admin.site.register(Stock)
admin.site.register(Tag)
