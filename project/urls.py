from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("create_book/", add_book,),
    path("create_author/", add_author,)
    
]