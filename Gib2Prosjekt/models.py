from django.db import models
from autoslug import AutoSlugField
#from geopy.geocoders import Nominatim
# Create your models here...
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.conf import settings


class Bolig(models.Model):
    address = models.CharField(max_length=100)
    desc = models.TextField()
    price=models.DecimalField(max_digits=100,decimal_places=1)
    slug = AutoSlugField(populate_from="address")
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    type = models.CharField(max_length=20, default='Enebolig')
    bedroom = models.IntegerField(default=2)
    energy = models.CharField(max_length=1, default='A')
    area = models.IntegerField(default=155)
    year = models.IntegerField(default=2012)

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
        fields = ('desc', 'price', 'type', 'bedroom', 'energy', 'area', 'year')
        labels={
            #'address': 'Skriv inn gatenummer og gateaddresse, Obs må være i Trondheim:',
            'desc': 'Gi en beskrivelse av boligen:',
            'price': 'Salgspris:',
            'type': 'Type bolig',
            'bedroom': 'antall soverom',
            'energy': 'Energiklassen',
            'area': 'antall kvadratmeter',
            'image': ''
        }
        widgets = {
            #'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'desc': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Desc'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type'}),
            'bedroom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bedroom'}),
            'energy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'energy'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'area'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'year'}),
            'image': forms.FileInput()
        }
