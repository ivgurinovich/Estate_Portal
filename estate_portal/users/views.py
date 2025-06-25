from django.shortcuts import render
from users.models import User
from properties.models import Property
from deals.models import Deal

def index(request):
    return render(request, 'index.html', {
        'user': User.objects.first(),
        'property': Property.objects.first(),
        'deal': Deal.objects.first(),
    })
