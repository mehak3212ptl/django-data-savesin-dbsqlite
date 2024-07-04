from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register),
    path('registerdata/',registerdata,name='register')
    
]