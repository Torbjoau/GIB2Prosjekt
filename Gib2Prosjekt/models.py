from django.db import models
from autoslug import AutoSlugField
#from geopy.geocoders import Nominatim
# Create your models here...
from django.forms import ModelForm
from django import forms

class Bolig(models.Model):
    address = models.CharField(max_length=100)
    desc = models.TextField()
    price=models.DecimalField(max_digits=100,decimal_places=1)
    slug = AutoSlugField(populate_from="address")
    #antall_sovrom = models.IntegerField(default=0)
    #energi_klasse = models.IntegerField(default=5)


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


class BoligForm(ModelForm):
    class Meta:
        model=Bolig
        fields = ('desc', 'price')
        labels={
            #'address': 'Skriv inn gatenummer og gateaddresse, Obs må være i Trondheim:',
            'desc': 'Gi en beskrivelse av boligen:',
            'price': 'Salgspris:',
        }
        widgets = {
            #'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'desc': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Desc'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}),
        }

