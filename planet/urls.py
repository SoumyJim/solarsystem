from django.contrib import admin
from django.urls import path, include
from planet.views import index

urlpatterns = [
    path('',index ),

]
