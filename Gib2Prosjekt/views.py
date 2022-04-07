from django.shortcuts import render
import folium
from geopy.geocoders import Nominatim
from .models import Bolig


# Create your views here.

def index(request):
    return render(request, 'index.html')

def hjem(request):
    list_bolig=Bolig.objects.all()
    return render(request, 'Bolig.html',
        {'list_bolig': list_bolig})


geolocator=Nominatim(user_agent="my_request")
v="Klostergata 18B,Trondheim,Norway"
print(v)
location=geolocator.geocode(v)
print((location.longitude, location.latitude))
l=geolocator.geocode("Roseveien 2,Lier,Norway")
p=geolocator.geocode("Kong Inges gate 3,Trondheim,Norway")



def kart(request):
    m = folium.Map(location=[63.417190066978264, 10.404224395751953], zoom_start=12)
    folium.Marker(location=[63.417190066978264, 10.404224395751953]).add_to(m)
    folium.Marker(location=[location.latitude,location.longitude]).add_to(m)
    folium.Marker(location=[l.latitude,l.longitude]).add_to(m)
    folium.Marker(location=[p.latitude,p.longitude]).add_to(m)
    hus=Bolig.objects.all()
    for i in hus:
        g=geolocator.geocode(i.address)
        folium.Marker(location=[g.latitude, g.longitude]).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'kart.html', context)
