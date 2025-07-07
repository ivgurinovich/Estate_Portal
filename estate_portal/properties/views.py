from django.shortcuts import render, get_object_or_404

from properties.models import Property


def property_list(request):
    properties_list = Property.objects.filter(available=True)
    return render(request, template_name='properties_list.html',
                  context={'properties_list': properties_list})


def property_detail(request, prop_id):
    prop_obj = get_object_or_404(Property, id=prop_id)
    return render(request, template_name='property_detail.html', context={'property': prop_obj})
