from django.shortcuts import render, get_object_or_404, redirect
import folium
from folium.plugins import MarkerCluster
import numpy as np
from geopy.geocoders import Nominatim
from .models import Bolig
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import BoligForm

from math import floor

import base64
import cgi

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hjem(request):
    list_bolig=Bolig.objects.all()
    return render(request, 'Bolig.html',
        {'list_bolig': list_bolig})

print('hello')

def bolig_view(request, slug):
    bolig_view = get_object_or_404(Bolig, slug=slug)
    return render(request, 'bolig_detail.html', {'bolig_view' : bolig_view})


#def update(request, slug):
#    bolig_view = get_object_or_404(Bolig, slug=slug)
#    return render(request, 'Update.html', {'bolig_view' : bolig_view})

geolocator=Nominatim(user_agent="my_request")


#hus = Bolig.objects.all()
#for i in hus:
#    print(i.address)
#    print(geolocator.geocode(i.address))

'''
def kart(request):
    m = folium.Map(location=[63.417190066978264, 10.404224395751953], zoom_start=12, hight=600, width=1800)
    #folium.Marker(location=[63.417190066978264, 10.404224395751953]).add_to(m)
    #folium.Marker(location=[location.latitude,location.longitude]).add_to(m)
    #folium.Marker(location=[l.latitude,l.longitude]).add_to(m)
    #folium.Marker(location=[p.latitude,p.longitude]).add_to(m)
    hus=Bolig.objects.all()
    for i in hus:
        g=geolocator.geocode(i.address+",Trondheim,Norway")
        html = folium.Html('<a href="http://127.0.0.1:8000/Bolig/' + i.slug + '" target="_blank">' + i.address + '</a>', script=True)
        #html = '<a href="../Bolig/%s"> test </a>'%i.slug
        iframe = folium.IFrame(html)
        Popup=folium.Popup(iframe, min_width=200, max_width=800)
        folium.Marker(location=[g.latitude, g.longitude], popup=Popup, icon=folium.Icon(color='red',style='white', icon='home')).add_to(m)


    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'kart.html', context)
'''




def kart(request):


    form_inputs = cgi.FieldStorage()
    m = folium.Map(location=[63.417190066978264, 10.404224395751953], zoom_start=12, hight=600, width='100%')
    marker_cluster = MarkerCluster().add_to(m)
    if request.method == 'POST':
        list = []
        type = request.POST.get("type")
        price = request.POST.get("price")
        area = request.POST.get("area")
        bedroom = request.POST.get("bedroom")
        energy = request.POST.get("energy")
        year = request.POST.get("year")

        price1 = request.POST.get("price_telle")
        type1 = request.POST.get("type")
        area1 = request.POST.get("area_telle")
        bedroom1 = request.POST.get("bedroom_telle")
        energy1 = request.POST.get("energy_telle")
        year1 = request.POST.get("year_telle")

        price_list = []
        for i in Bolig.objects.all():
            price_list.append(i.price)
        tot_max_price = max(price_list)
        tot_min_price = min(price_list)
        print("maks pris: ", tot_max_price, " min pris: ", tot_min_price)

        if type == 'alle':
            for i in Bolig.objects.all():
                if ((i.price < float(price or 0) or form_inputs.getvalue("price") is None )) and (i.area > int(area or 0)) and (i.bedroom >= int(bedroom or 0)) and (energy != "true" or (ord(i.energy) <= ord(energy))) and (i.year >= int(year or 0)):
                    list.append(i)
        else:
            for i in Bolig.objects.all():
                if ((i.price < float(price or 0) or form_inputs.getvalue("price") is None )) and (i.area > int(area or 0)) and i.type == type and (i.bedroom >= int(bedroom or 0)) and (energy != "true" or (ord(i.energy) <= ord(energy))) and (i.year >= int(year or 0)):
                    list.append(i)


        #return redirect('kart')
        print(list)
        print(float(price or 0))
        print(int(year or 0))
        print(type)
        #hus=Bolig.objects.all()

        max_points = 0
        min_points = 99999999999
        list_points = []
        for i in list:
            print("NY BOLIG")
            points = 0
            #Dersom energiklasse er valgt, men ikke huket av for høy energiklasse
            if energy1 != "true" and energy != "true":
                print("alt1_energi")
                if i.energy == 'A' or i.energy == 'B':
                    points += 3
                elif i.energy == 'C' or i.energy == 'D':
                    points += 2
                else:
                    points += 1
            #Derson energiklasse er valgt og huket av for høy energiklasse eller kun huket av for høy energiklasse
            if (energy1 == "true" and energy != "true") or (energy1 == "true" and energy == "true"):
                if i.energy == 'A' or i.energy == 'B':
                    points += 3*2
                elif i.energy == 'C' or i.energy == 'D':
                    points += 2*2
                else:
                    points += 1*2
            print("Poeng energi: ", points)

            if int(bedroom or 0) != 0 and bedroom1 == "true":
                print("alt1_sov")
                if i.bedroom == 5:
                    points += 3
                elif i.bedroom == 4 or i.bedroom == 3:
                    points += 2
                else:
                    points += 1
            elif int(bedroom or 0) == 0 and bedroom1 != "true":
                print("alt2_sov")
                points += 0
            elif int(bedroom or 0) != 0 and bedroom1 != "true":
                print("alt3_sov")
                if i.bedroom == int(bedroom):
                    points += 3
                elif i.bedroom == (int(bedroom) + 1):
                    points += 2
                else:
                    points += 1

            #Dersom byggeår er gitt og ikke ønsker nytt hus
            if int(year or 0) != 0 and year1 != "true":
                print("alt1_bygg")
                if i.year >= int(year or 0)+15:
                    points += 3
                elif int(year)+10 <= i.year < int(year or 0)+15:
                    points += 2
                else:
                    points += 1
            #Dersom byggeår er gitt og ønsker nytt hus = legg til vekting
            if int(year or 0) != 0 and year1 == "true":
                print("alt2_bygg")
                if i.year >= int(year or 0)+15:
                    points += 3*2
                elif int(year)+10 <= i.year < int(year or 0)+15:
                    points += 2*2
                else:
                    points += 1*2
            #Dersom byggeår ikke er gitt, men ønsker nytt hus = bruk gitte intervaller
            if int(year or 0) == 0 and year1 == "true":
                print("alt3_bygg")
                if i.year >= 2010:
                    points += 3
                elif 1990 < int(i.year) <= 1990:
                    points += 2
                else:
                    points += 1

            print("poeng før pris: ", points)
            #Dersom makspris er fylt ut og ikke ønsker lav pris = flest poeng til boliger nærmest makspris
            if float(price or 0) != 0 and price1 != "true":
                print("alt1")
                if i.price >= 3*int(price)/4:
                    points += 3
                elif i.price >= int(price)/2:
                    points += 2
                else:
                    points += 1
            #Dersom makspris er fylt ut, men ønsker lav pris = flest poeng til bolig med lavest pris
            elif float(price or 0) != 0 and price1 == "true":
                print("alt2")
                if i.price <= int(price)/3:
                    points += 3
                elif i.price <= 2*int(price)/3:
                    points += 2
                else:
                    points += 1
            #Dersom makspris ikke er fylt ut, men ønsker lav pris = flest poeng til bolig med lavest pris (ser på hele databasen)
            elif float(price or 0) == 0 and price1 == "true":
                print("alt3")
                if i.price <= tot_min_price + (tot_max_price-tot_min_price)/3:
                    points += 3
                elif i.price <= tot_min_price + (2*(tot_max_price-tot_min_price))/3:
                    points += 2
                else:
                    points += 1
            print("poeng etter pris: ", points)
            list_points.append(points)
            if points > max_points:
                max_points = points
            if points < min_points:
                min_points = points
        print("maks: ", max_points, " min: ", min_points)
        print("darkred:", min_points + 3*(max_points-min_points)/4, " red:", min_points + (max_points-min_points)/2, " lightred:", min_points + (max_points - min_points)/4)

        i = 0
        for item in list:
            g=geolocator.geocode(item.address+",Trondheim,Norway")
            #html = folium.Html('<a href="http://127.0.0.1:8000/Bolig/' + item.slug + '" target="_blank">' + item.address + '</a>', "<img scr="+str(item.image)+"/>")#, script=True)


            encoded = base64.b64encode(open("media/" + str(item.image), 'rb').read())
            # html = '<img src="data:image/jpeg;base64,{}" width=250 height=250>'.format
            html = f'''

                    <h1 style="font-family: 'Century Gothic'"> {item.address} </h1>
                    <a href="http://127.0.0.1:8000/Bolig/{item.slug}" target="_blank"> <img src="data:image/jpeg;base64,{{}}" height=250> </a>

                    '''.format
            iframe = folium.IFrame(html(encoded.decode('UTF-8')), width=400, height=350)

            #iframe = folium.IFrame(html)
            print(item.image)
            Popup=folium.Popup(iframe, min_width=200, max_width=800)

            if list_points[i] >= min_points + 3*(max_points-min_points)/4:
                folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer informasjon", icon=folium.Icon(color='darkred', icon='home')).add_to(marker_cluster)
            elif min_points + (max_points-min_points)/2 <= list_points[i] < min_points + 3*(max_points-min_points)/4:
                folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer informasjon", icon=folium.Icon(color='red', icon='home')).add_to(marker_cluster)
            elif min_points + (max_points - min_points)/4 <= list_points[i] < min_points + (max_points - min_points)/2:
                folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer informasjon", icon=folium.Icon(color='lightred', icon='home')).add_to(marker_cluster)
            else:
                folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer informasjon", icon=folium.Icon(color='white', icon='home')).add_to(marker_cluster)
            
            i += 1
        m = m._repr_html_()
        context = {
            'm': m,
        }
        return render(request, 'kart.html', context)
    else:
        hus=Bolig.objects.all()
        for i in hus:
            g=geolocator.geocode(i.address+",Trondheim,Norway")
            encoded = base64.b64encode(open("media/" + str(i.image), 'rb').read())
            # html = '<img src="data:image/jpeg;base64,{}" width=250 height=250>'.format
            html = f'''

                                <h1 style="font-family: 'Century Gothic'"> {i.address} </h1>
                                <a href="http://127.0.0.1:8000/Bolig/{i.slug}" target="_blank"> <img src="data:image/jpeg;base64,{{}}" height=250> </a>

                                '''.format
            iframe = folium.IFrame(html(encoded.decode('UTF-8')), width=400, height=350)

            # iframe = folium.IFrame(html)
            Popup = folium.Popup(iframe, min_width=200, max_width=800)
            folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer informasjon",
                          icon=folium.Icon(color='red', icon='home')).add_to(marker_cluster)

        m = m._repr_html_()
        context = {
            'm': m,
        }
        return render(request, 'kart.html', context)



def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('log_in')
        else:
            messages.info(request, 'passordene er ikke like')
            return redirect('register')

    else:
        return render(request,'register.html')


def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid')
            return render(request,'log_in.html')

    else:
        return render(request,'log_in.html')


def log_out(request):
    auth.logout(request)
    return redirect('index')


def lage_bolig_annonse(request):
        if request.method == 'POST':
            owner= request.user
            address = request.POST['address']
            desc = request.POST['desc']
            price = request.POST['price']
            image = request.FILES['image']

            type = request.POST['type']
            energy = request.POST['energy']
            area = request.POST['area']
            year = request.POST['year']
            bedroom=request.POST['bedroom']

            hus=Bolig(
                address=address,
                desc=desc,
                price=price,
                owner=owner,
                image=image,
                type=type,
                bedroom=bedroom,
                energy=energy,
                area=area,
                year=year
            )
            location1=geolocator.geocode(address+",Trondheim,Norway")
            print(location1)
            print(address)
            print((location1.latitude,location1.longitude))
            try:
                print((location1.latitude,location1.longitude))
                if Bolig.objects.filter(address=address).exists():
                    messages.info(request,'Addresse er opptatt')
                    return redirect('lage_bolig_annonse')
                    print('exists')
                else:
                    hus.save()
                    print('hello1')
                    return redirect('Bolig')
                    print('saved')
                print('hello2')
            except:
                print("wrong address!")
                messages.info(request, 'Wrong address!')
                return render(request,'lage_bolig_annonse.html')

        else:
            return render(request,'lage_bolig_annonse.html')

def update(request, slug):
    bolig_update=get_object_or_404(Bolig, slug=slug)
    form=BoligForm(request.POST or None, instance=bolig_update)
    if form.is_valid():
        form.save()
        return redirect('Bolig')
    return render(request,'Update.html',{'bolig_update': bolig_update,'form':form})
 #   return render(request,'update.html',{'bolig': bolig_update})



def delete(request, slug):
    bolig_update = get_object_or_404(Bolig, slug=slug)
     #bolig_update.delete()
    return render(request, 'Delete.html', {'bolig_update':bolig_update})

def delete2(request, slug):
    bolig_update = get_object_or_404(Bolig, slug=slug)
    bolig_update.delete()
    return redirect('Bolig')

