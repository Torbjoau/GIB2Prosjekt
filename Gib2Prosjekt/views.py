import base64

from django.shortcuts import render, get_object_or_404
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


def bolig_view(request, slug):
    bolig_view = get_object_or_404(Bolig, slug=slug)
    return render(request, 'bolig_detail.html', {'bolig_view' : bolig_view})

geolocator=Nominatim(user_agent="my_request")
v="Klostergata 18B,Trondheim,Norway"
print(v)
location=geolocator.geocode(v)
print((location.longitude, location.latitude))
l=geolocator.geocode("Roseveien 2,Lier,Norway")
p=geolocator.geocode("Kong Inges gate 3,Trondheim,Norway")

#hus = Bolig.objects.all()
#for i in hus:
#    print(i.address)
#    print(geolocator.geocode(i.address))

def kart(request):
    m = folium.Map(location=[63.417190066978264, 10.404224395751953], zoom_start=12)
    folium.Marker(location=[63.417190066978264, 10.404224395751953]).add_to(m)
    folium.Marker(location=[location.latitude,location.longitude]).add_to(m)
    folium.Marker(location=[l.latitude,l.longitude]).add_to(m)
    folium.Marker(location=[p.latitude,p.longitude]).add_to(m)
    hus=Bolig.objects.all()
    for i in hus:
        g=geolocator.geocode(i.address)

        encoded = base64.b64encode(open("media/" + str(i.image), 'rb').read())
        #html = '<img src="data:image/jpeg;base64,{}" width=250 height=250>'.format
        html = f'''
        
        <h1 style="color:red;"> {i.address} </h1> 
        <a href="http://127.0.0.1:8000/Bolig/{i.slug}" target="_blank"> <img src="data:image/jpeg;base64,{{}}" width=250 height=250> </a>
        
        '''.format
        iframe = folium.IFrame(html(encoded.decode('UTF-8')), width=400, height=350)
        Popup=folium.Popup(iframe, min_width=200, max_width=300)

        folium.Marker(location=[g.latitude, g.longitude], popup=Popup, icon=folium.Icon(color='lightgray', icon='home')).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'kart.html', context)
