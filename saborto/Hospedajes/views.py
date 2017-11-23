from django.shortcuts import render
from models import *
import datetime

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def search_rooms_view(request):
    if request.method == 'GET':
        return render(request, 'search_rooms.html')

def show_rooms_view(request):
    if request.method == 'GET':
        city = City.objects.get(name = request.GET['city'])
        pax = request.GET['pax']
        date1 = request.GET['date']
        print date1
        property = Property.objects.filter(city = city, maxGuest__gte = pax)

        aux = []
        for i in property:
            property2 =  DateRental.objects.get(property = property, date = datetime.datetime.strptime(date1,'%Y-%m-%d').date())
            aux.append(property2)

        for indice in range(len(property)):
            property[indice].comision = property[indice].priceDays * 0.08

        return render(request, 'show_rooms.html', {'rooms': aux})


