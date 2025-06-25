from django.urls import path
from deals.views import index

urlpatterns = [
    path('', index)
]