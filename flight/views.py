from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.


def index(request):
    context = {
        'flights': Flight.objects.all()
    }
    return render(request, 'flights/index.html', context)

def flight(request, flight_id):
    flight_obj = get_object_or_404(Flight, pk=flight_id)
    context = {
        'flight': flight_obj,
        'passengers': flight_obj.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight_obj).all()
    }
    return render(request, 'flights/flight.html', context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST['passenger'])
    except KeyError:
        return render(request, 'flights/error.html', { 'message': 'No selection' })
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    flight_obj = get_object_or_404(Flight, pk=flight_id)
    passenger.flights.add(flight_obj)
    return HttpResponseRedirect(reverse('flight', kwargs={'flight_id': flight_id}))
