from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import datetime
from .models import Flights,Airport,Passenger


def flight_details(request):
	context = {
		"flights" : Flights.objects.all(),
	}
	return render(request,"flights/index.html",context)

def this_flight(request,flight_idd):
	try:
		flight = Flights.objects.get(pk=flight_idd)
	except Flights.DoesNotExist:
		raise Http404("Flight not found.")
	context={
		"fl_det": flight,
		"passengers" : flight.passengers.all(),
		"non_passengers" : Passenger.objects.exclude(flights=flight).all(),
	}

	return render(request,"flights/thisflight.html",context)

def book_flight(request,flight_idd):
	try:
		passenger_id = int(request.POST["passenger"])
		passenger = Passenger.objects.get(pk=passenger_id)
		flights=Flights.objects.get(pk=flight_idd)

	except KeyError:
		return render(request,"flights/error.html",{"message":"No selection"})
	except Passenger.DoesNotExist:
		return render(request,"flights/error.html",{"message":"Passenger Does Not Exist"})
	except Flights.DoesNotExist:
		return render(request,"flights/error.html",{"message":"Flight Does Not Exist"})

	passenger.flights.add(flights)
	
	return HttpResponseRedirect(reverse("flight",args=(flight_idd,)))



