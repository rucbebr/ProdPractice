from .views import *
from django.urls import path

urlpatterns = [
    path('', index),
    path('lol/', hack),
]