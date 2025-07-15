from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from properties.models import Property, DealRequest
from django.contrib.auth.decorators import login_required
from properties.forms import DealRequestForm, PropertyForm


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
        property__owner=request.user
    ).order_by("-created_at")

    return render(request, 'owner_requests.html', {
        'deal_requests': deal_requests
    })


@login_required
def seeker_request_list(request):
    deal_requests = DealRequest.objects.select_related('property', 'property__owner').filter(
        seeker=request.user).order_by("-created_at")
    return render(request, 'seeker_requests.html', {'deal_requests': deal_requests})


@require_POST
@login_required
def change_request_status(request, req_id, new_status):
    deal_request = get_object_or_404(DealRequest, id=req_id, property__owner=request.user)

    if new_status in ['approved', 'rejected']:
        deal_request.status = new_status
        deal_request.save()
    return redirect('properties:owner_request_list')


@login_required
def create_property(request):
    if not request.user.is_owner():
        return redirect('properties:property_list')
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.save()
            return redirect('properties:detail', prop_id=property_obj.pk)

    else:
        form = PropertyForm()
    return render(request, 'property_form.html',
                  {'form': form})


@login_required
def edit_property(request, prop_id):
    property_obj = get_object_or_404(Property, id=prop_id, owner=request.user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            return redirect('properties:detail', prop_id=property_obj.pk)
    else:
        form = PropertyForm(instance=property_obj)

    return render(request, 'property_form.html', {'form': form})
