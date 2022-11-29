from django.urls import path

from .views import LamaPage

urlpatterns = [
    path('', LamaPage, name='LamaPage'),
]