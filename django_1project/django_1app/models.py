from django.db import models

# Create your models here
class Test_Model1(models.Model):
	title=models.CharField(max_length=200)
	name=models.TextField()
	last_modified=models.DateTimeField(auto_now_add=True)
	image_field=models.ImageField(upload_to='images/')

	def __str__(self):
		return "{} - {}".format(self.title,self.name)



class Airport(models.Model):
	city=models.CharField(max_length=64)
	code=models.CharField(max_length=64)

	def __str__(self):
		return "{}({})".format(self.city,self.code)


class Flights(models.Model):
	origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
	destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")

	def __str__(self):
		return f"{self.origin} - {self.destination}"


class Passenger(models.Model):
	first=models.CharField(max_length=64)
	last=models.CharField(max_length=64)
	flights=models.ManyToManyField(Flights,blank=True,related_name="passengers")

	def __str__(self):
		return "{} {}".format(self.first,self.last)
