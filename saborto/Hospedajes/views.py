from django.shortcuts import render
from Hospedajes.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search_rooms_view(request):
    return render(request, 'search_rooms.html')

def show_rooms_view(request):
	habitacion_mockeada=Property(description='esta re piola man te re combiene', priceDays=500, image='', title='casa super cheta por la perla', numberCard=0, maxGuest=20, city=City(name='Mar del Plata'), user=User())
	return render(request, 'show_rooms.html', {'rooms': habitacion_mockeada})
