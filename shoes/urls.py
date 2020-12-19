from django.contrib import admin
from django.urls import path, include

import shoes.views

urlpatterns = [
    path('', shoes.views.index, name='main_shoe'),
    path('main', shoes.views.main),
    path('view', shoes.views.view_shoe),
    path('viewnew', shoes.views.view_newshoe),
    path('create', shoes.views.create_shoe),
    path('createnew', shoes.views.create_newshoe),
    path('edit_shoe/<shoe_id>', shoes.views.edit_shoe,
         name='shoe_update'),
    path('edit_newshoe/<newShoe_id>', shoes.views.edit_newshoe,
         name='newshoe_update'),
    path('delete_shoe/<shoe_id>', shoes.views.delete_shoe,
         name='delete_shoe'),
    path('delete_newshoe/<newShoe_id>',
         shoes.views.delete_newshoe, name='delete_newshoe'),
]
