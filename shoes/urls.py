from django.contrib import admin
from django.urls import path

import shoes.views

urlpatterns = [
    path('', shoes.views.index, name='main_shoe'),
    path('home_consumer', shoes.views.home_consumer, name='home_consumer'),
    path('success', shoes.views.home, name='home_page'),
    path('main', shoes.views.main, name='consumer_page'),
    path('info/<shoe_id>', shoes.views.shoe_info, name='view_shoe_info'),
    path('consumer_info/<shoe_id>', shoes.views.consumer_shoe_info,
         name='consumer_shoe_info'),
    path('create_shoe', shoes.views.create_shoe, name='create_shoe'),
    path('edit_shoe/<shoe_id>', shoes.views.edit_shoe,
         name='shoe_update'),
    path('delete_shoe/<shoe_id>', shoes.views.delete_shoe,
         name='delete_shoe'),
    path('contact', shoes.views.contact, name='contact'),
    path('admin', admin.site.index, name='admin'),

]
