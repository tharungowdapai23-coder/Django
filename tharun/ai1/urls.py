
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.chai),
    path("<int:chai_id>", views.details, name="details"),
    
]

