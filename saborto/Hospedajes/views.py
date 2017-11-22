from django.shortcuts import render
from models import *

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def search_rooms_view(request):
    if request.method == 'GET':
        return render(request, 'search_rooms.html')

def show_rooms_view(request):
    if request.method == 'GET':
        city = City.objects.filter(name = request.GET['city'])
        pax = request.GET['pax']
        date1 = request.GET['date']
        print date1
        property = Property.objects.filter(city = city[0].id, maxGuest__gte = pax)

        '''property = DateRental.objects.select_related(id = property_id)'''
        print property

        for indice in range(len(property)):
            property[indice].comision = property[indice].priceDays * 0.08

        return render(request, 'show_rooms.html', {'rooms': property})


