from django.urls import path
from properties.views import (property_list, property_detail, create_deal_request,owner_request_list,seeker_request_list,change_request_status,create_property,
                              property_detail,edit_property)



app_name = 'properties'

urlpatterns = [
    path('', property_list, name='property_list'),
    path('<int:prop_id>/', property_detail, name='detail'),
    path("<int:prop_id>/request/", create_deal_request, name='deal_request'),
    path('my_requests/', owner_request_list, name='owner_request_list'),
    path('seeker_requests/', seeker_request_list, name='seeker_request_list'),
    path('my_applications/', seeker_request_list, name='seeker_my_applications'),
    path('change_status/<int:req_id>/<str:new_status>/', change_request_status, name='change_request_status'),
    path('property_create/', create_property, name='create_property'),
    path('property_edit/<int:prop_id>/', edit_property, name='edit_property'),




]
