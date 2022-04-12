from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kart/', views.kart, name = 'kart'),
    path('Bolig/', views.hjem, name='Bolig'),
    path('Bolig/<slug:slug>/', views.bolig_view, name='profile'),

]