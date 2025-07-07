from django.urls import path
from properties.views import property_list, property_detail

app_name = 'properties'

urlpatterns = [
    path('', property_list, name='property_list'),
    path('<int:prop_id>/', property_detail, name='detail')
]
