from django.shortcuts import render
from deals.models import Deal


def index(request):
    test_deal = Deal.objects.first()
    return render(request, 'index.html',
                  context={'deal': test_deal})
