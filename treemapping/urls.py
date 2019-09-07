from django.urls import path
from . import views

urlpatterns = [
    path('', views.maptree, name='maptree'),
]