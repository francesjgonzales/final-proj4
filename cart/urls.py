from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, edit_quantity

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<shoe_id>', add_to_cart, name='add_to_cart'),
    path('remove/<shoe_id>', remove_from_cart, name='remove_from_cart'),
    path('edit/<shoe_id>', edit_quantity, name='edit_cart')

]
