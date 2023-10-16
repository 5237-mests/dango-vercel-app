# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mydjv/', views.my_view, name='ap2'),
]
