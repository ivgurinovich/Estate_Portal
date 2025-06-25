from django.shortcuts import render
from properties.models import Property


def index(request):
    test_prop = Property.objects.first()
    return render(request, 'index.html',
                  context={'property': test_prop})
