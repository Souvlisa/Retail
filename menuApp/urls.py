from django.urls import path
from menuApp import views

urlpatterns = [
    path('', views.menu, name='menu'),
]