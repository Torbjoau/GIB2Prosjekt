from django.urls import path, re_path
from .import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.kart, name = 'kart'),
    path('Bolig/', views.hjem, name='Bolig'),
    path('Bolig/<slug:slug>/', views.bolig_view, name='profile'),
    path('register', views.register, name='register'),
    path('log_in',views.log_in,name='log_in'),
    path('log_out',views.log_out,name='log_out'),
    path('lage_bolig_annonse', views.lage_bolig_annonse, name='lage_bolig_annonse'),
    path('Bolig/<slug:slug>/Update', views.update, name='Update'),
    path('Bolig/<slug:slug>/Delete', views.delete, name='Delete'),
    path('Bolig/<slug:slug>/Delete2', views.delete2, name='Delete2'),
    #path('valg/', views.valg, name='valg'),
    #path('Bolig2/<slug:slug>/', views.update, name='update'),
]