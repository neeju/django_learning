from django.contrib import admin

# Register your models here.
from .models import Test_Model1,Airport,Flights,Passenger
admin.site.register(Test_Model1)
admin.site.register(Airport)
admin.site.register(Flights)
admin.site.register(Passenger)