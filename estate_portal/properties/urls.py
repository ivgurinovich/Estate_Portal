from django.urls import path
from properties.views import property_list, property_detail, create_deal_request,owner_request_list

app_name = 'properties'

urlpatterns = [
    path('', property_list, name='property_list'),
    path('<int:prop_id>/', property_detail, name='detail'),
    path("<int:prop_id>/request", create_deal_request, name='deal_request'),
    path('my_requests/', owner_request_list, name='owner_request_list'),
]
