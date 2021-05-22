from .views import *
from django.urls import path


urlpatterns = [
    path('predictOnTow', predictOnTwoImage),
    path('predictOnOne', predictOnOneImage)
]
