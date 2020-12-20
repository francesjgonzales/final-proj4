from django.contrib import admin
from django.urls import path, include
import reviews.views

urlpatterns = [
    path('', reviews.views.index),
    path('write/<shoe_id>', reviews.views.write_review, name='write_review_route'),
]
