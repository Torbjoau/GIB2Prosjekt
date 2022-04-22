from django.shortcuts import render, get_object_or_404, redirect
import folium
from geopy.geocoders import Nominatim
from .models import Bolig
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import BoligForm
from math import floor

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
    m = folium.Map(location=[63.417190066978264, 10.404224395751953], zoom_start=12, hight=600, width=1800)
    if request.method == 'POST':
        list = []
        type = request.POST.get("type")
        for i in Bolig.objects.all():
            if i.type == type:
                list.append(i)
        #return redirect('kart')
        price = request.POST.get("price_telle")
        type = request.POST.get("type")
        area = request.POST.get("area_telle")
        bedroom = request.POST.get("bedroom_telle")
        energy = request.POST.get("energy_telle")
        year = request.POST.get("year_telle")
        #hus=Bolig.objects.all()
        for i in list:
            g=geolocator.geocode(i.address+",Trondheim,Norway")
            html = folium.Html('<a href="http://127.0.0.1:8000/Bolig/' + i.slug + '" target="_blank">' + i.address + '</a>', script=True)
            #html = '<a href="../Bolig/%s"> test </a>'%i.slug
            iframe = folium.IFrame(html)
            Popup=folium.Popup(iframe, min_width=200, max_width=800)
            l=0
            nr=0
            if price =='true':
                if int(i.price) <= 2000000:
                    nr_p=4
                elif 2000000 < int(i.price) <= 5000000:
                    nr_p=3
                elif 5000000 < int(i.price) <= 9000000:
                    nr_p=2
                else:
                    nr_p=1
                l+=1
                nr+=nr_p

            if energy == 'true':
                if str(i.energy) =='A':
                    nr_e=4
                elif str(i.energy) == 'B':
                    nr_e=3
                elif str(i.price) == 'C':
                    nr_e=2
                else:
                    nr_e=1
                l+=1
                nr+=nr_e
            if area == 'true':
                if int(i.area) >= 120:
                    nr_a=4
                elif 80 < int(i.area) <= 120:
                    nr_a=3
                elif 40 < int(i.area) <= 80:
                    nr_a=2
                else:
                    nr_a=1
                l+=1
                nr+=nr_a
            if year == 'true':
                if int(i.year) >= 2010:
                    nr_y = 4
                elif 1990 < int(i.year) <= 2010:
                    nr_y = 3
                elif 1960 < int(i.year) <= 1990:
                    nr_y = 2
                else:
                    nr_y = 1
                l += 1
                nr += nr_y
            if bedroom == 'true':
                if int(i.bedroom) >= 4:
                    nr_b = 4
                elif 3 < int(i.year) <= 4:
                    nr_b = 3
                elif 2 < int(i.year) <= 3:
                    nr_b = 2
                else:
                    nr_b = 1
                l += 1
                nr += nr_b
            if l !=0:
                nr=int(floor(nr/l))
                print(nr)
            else:
                nr=3

            if nr==4:
                folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer infromasjon", icon=folium.Icon(color='darkred', icon='home')).add_to(m)
            elif nr==3:
                folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer infromasjon", icon=folium.Icon(color='red', icon='home')).add_to(m)
            elif nr==2:
                folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer infromasjon", icon=folium.Icon(color='lightred', icon='home')).add_to(m)
            else:
                folium.Marker(location=[g.latitude, g.longitude], popup=Popup, tooltip="trykk for mer infromasjon", icon=folium.Icon(color='white', icon_color="gray", icon='home')).add_to(m)

        m = m._repr_html_()
        context = {
            'm': m,
        }
        return render(request, 'kart.html', context)
    else:
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
            address = request.POST['address']
            desc = request.POST['desc']
            price = request.POST['price']
            hus=Bolig(
                address=address,
                desc=desc,
                price=price)
            location1=geolocator.geocode(address+",Trondheim,Norway")
            try:
                print((location1.latitude,location1.longitude))
                if Bolig.objects.filter(address=address).exists():
                    messages.info(request,'Addresse er opptatt')
                    return redirect('lage_bolig_annonse')
                else:
                    hus.save()
                    return redirect('Bolig')
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

def valg(request):
    if request.method == 'POST':
        price = request.POST.get("price")
        type = request.POST.get("type")
        area = request.POST.get("area")
        bedrooms = request.POST.get("bedrooms")
        energy = request.POST.get("energy")
        print(price, type, area, bedrooms, energy)
        l=[]
        for i in Bolig.objects.all():

            if (i.price < float(price or 0)) and (i.area > int(area or 0)) and (i.bedroom >= int(bedrooms or 0)) and (i.type == type) and (ord(i.energy) <= ord(energy)):
            #if i.type == type:
                l.append(i)
        print(l)
        return redirect('kart')
    else:
        return render(request, 'valg.html')



