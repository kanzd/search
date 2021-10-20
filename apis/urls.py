from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('search/',views.SearchAPI.as_view())
]




