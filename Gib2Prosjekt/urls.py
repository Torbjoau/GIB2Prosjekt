from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kart/', views.kart, name = 'kart'),
    path('Bolig/', views.hjem, name='Bolig'),
    path('Bolig/<slug:slug>/', views.bolig_view, name='profile'),
    path('register', views.register, name='register'),
    path('log_in',views.log_in,name='log_in'),
    path('log_out/',views.log_out,name='log_out'),
    path('lage_bolig_annonse/',views.lage_bolig_annonse, name='lage_bolig_annonse'),
]