from django.urls import path
from properties.views import property_list, property_detail

from estate_portal.properties.views import create_deal_request

app_name = 'properties'

urlpatterns = [
    path('', property_list, name='property_list'),
    path('<int:prop_id>/', property_detail, name='detail')
    path("<int:prop_id>/request", create_deal_request, name='deal_request')
]
