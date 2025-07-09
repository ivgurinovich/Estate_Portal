from django.shortcuts import render, get_object_or_404, redirect
from properties.models import Property, DealRequest
from django.contrib.auth.decorators import login_required
from properties.forms import DealRequestForm


def property_list(request):
    properties_list = Property.objects.filter(available=True)
    return render(request, template_name='properties_list.html',
                  context={'properties_list': properties_list})


def property_detail(request, prop_id):
    prop_obj = get_object_or_404(Property, id=prop_id)
    return render(request, template_name='property_detail.html', context={'property': prop_obj})


def create_deal_request(request, prop_id):
    property_obj = get_object_or_404(Property, id=prop_id)

    if request.method == 'POST':
        form = DealRequestForm(request.POST)
        if form.is_valid():
            deal_request = form.save(commit=False)
            deal_request.seeker = request.user
            deal_request.property = property_obj
            deal_request.save()
            return redirect('properties:detail', prop_id=prop_id)
    else:
        form = DealRequestForm()

    return render(request, 'deal_request_form.html', {
        'form': form,
        'property': property_obj
    })


@login_required
def owner_request_list(request):
    deal_requests = DealRequest.objects.select_related('property', 'seeker').filter(
        property__owner=request.user).order_by("-created_at")
    return render(request, template_name='owner_requests.html',
                  context={'deal_requests': deal_requests})
