from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kart/', views.kart, name = 'kart'),
    path('Bolig/', views.hjem, name='Bolig'),
]