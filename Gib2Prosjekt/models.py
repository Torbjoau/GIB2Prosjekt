from django.db import models
#from geopy.geocoders import Nominatim
# Create your models here.
#geolocator=Nominatim(user_agent='my_request')
#ad="Klostergata 1"
#locat=geolocator.geocode(str(ad)+',Trondheim,Norway')
#print((locat.latitude, locat.longitude))
        #lat=location.latitude
        #long=location.longitude
        #print(location)


class Bolig(models.Model):
    address = models.CharField(max_length=100)
    desc = models.TextField()
    price=models.DecimalField(max_digits=100,decimal_places=1)
    #lat = models.DecimalField(max_digits=9, decimal_places=6) #breddegrad
    #long= models.DecimalField(max_digits=9, decimal_places=6) #lengdegrad
    #long=models.CharField(str(address)+'Trondheim,Norway',max_length=100)
    #if address=='':
        #address="Klostergata 1"
    #else:
        #location=geolocator.geocode(str(address)+',Trondheim,Norway')
        #print((location.latitude, location.longitude))
        #lat=location.latitude
        #long=location.longitude
        #print(location)
    #print(lat,long)


#class Hus(models.Model):
    #address = models.CharField(max_length=100)
    #location=geolocator.geocode(address+',Trondheim,Norway')
    #lat=location.latitude
    #long=location.longitude




