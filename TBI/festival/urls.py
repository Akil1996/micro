from django.urls import path
from . import views

urlpatterns = [
    path('', views.festival_home, name="festivalHome"),
]
