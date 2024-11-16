from django.shortcuts import render

# Create your views here.
from django.db.models import Count, F, Sum, Value

from .models import Room, Registration

def rooms_with_tv(request):
    rooms = Room.objects.filter(tv=True)
    return render(request, 'rooms_with_tv.html', {'rooms': rooms})

def total_stay_cost(request):
    guests = Registration.objects.annotate(
        total_cost=F('days_of_stay') * F('room__price_per_day')
    )
    return render(request, 'total_stay_cost.html', {'guests': guests})
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
