"""TheNewSoleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import shoes.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('shoes/', shoes.views.index, name='main_shoe'),
    path('shoes/create', shoes.views.create_shoe),
    path('shoes/createnew', shoes.views.create_newshoe),
    path('shoes/edit_shoe/<shoe_id>', shoes.views.edit_shoe,
         name='shoe_update'),
    path('shoes/edit_newshoe/<newShoe_id>', shoes.views.edit_newshoe,
         name='newshoe_update'),
    path('shoes/delete_shoe/<shoe_id>', shoes.views.delete_shoe,
         name='delete_shoe'),
    path('shoes/delete_newshoe/<newShoe_id>',
         shoes.views.delete_newshoe, name='delete_newshoe')
]
