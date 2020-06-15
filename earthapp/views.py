from django.shortcuts import render
from earthapp.models import Earthapp


def index(request):
    earthapp = Earthapp.objects.all()
    return render(request, 'index.html', {'earthapp': earthapp})
