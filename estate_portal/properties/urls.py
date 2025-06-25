from django.urls import path
from properties.views import index

urlpatterns = [
    path('', index)
]