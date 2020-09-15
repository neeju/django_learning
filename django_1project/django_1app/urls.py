from django.urls import path,include
from .views import flight_details,this_flight,book_flight

urlpatterns = [
	path('all_flights/',flight_details,name="index"),
	path("flights/<int:flight_idd>/",this_flight,name="flight"),
	path("flights/<int:flight_idd>/book/",book_flight,name="bookflight"),
	
	]
