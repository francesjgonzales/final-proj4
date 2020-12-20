from django.contrib import admin
from django.urls import path, include

import shoes.views

urlpatterns = [
    path('', shoes.views.index, name='main_shoe'),
    path('main', shoes.views.main, name='consumer_page'),
    path('info/<shoe_id>', shoes.views.shoe_info),
    path('create', shoes.views.create_shoe, name='create_shoe'),
    path('edit_shoe/<shoe_id>', shoes.views.edit_shoe,
         name='shoe_update'),
    path('delete_shoe/<shoe_id>', shoes.views.delete_shoe,
         name='delete_shoe'),
]
