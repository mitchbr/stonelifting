from django.urls import path
from . import views

app_name = 'stones'

urlpatterns = [
    path('', views.index, name='index'),
    path('traffic', views.traffic, name='traffic'),
]
