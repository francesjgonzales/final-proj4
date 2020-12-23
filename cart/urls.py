from django.urls import path
import cart.views

urlpatterns = [
    path('view/', cart.views.view_cart, name='view_cart'),
    path('add/<shoe_id>', cart.views.add_to_cart, name='add_to_cart'),
    path('remove/<shoe_id>', cart.views.remove_from_cart, name='remove_from_cart'),
    path('edit/<shoe_id>', cart.views.edit_quantity, name='edit_cart')

]
