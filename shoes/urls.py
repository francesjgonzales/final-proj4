from django.contrib import admin
from django.urls import path, include

import shoes.views

urlpatterns = [
    path('', shoes.views.index, name='main_shoe'),
    path('main', shoes.views.main),
    path('info', shoes.views.shoe_info),
    path('view', shoes.views.view_shoe),
    path('create', shoes.views.create_shoe),
    path('edit_shoe/<shoe_id>', shoes.views.edit_shoe,
         name='shoe_update'),
    path('delete_shoe/<shoe_id>', shoes.views.delete_shoe,
         name='delete_shoe'),
]
