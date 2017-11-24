from django.shortcuts import render, render_to_response
from models import *
import datetime
import random

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'search_rooms.html')

def search_rooms_view(request):
    if request.method == 'GET':
        return render(request, 'search_rooms.html')

def show_rooms_view(request):
    if request.method == 'GET':
        try:
            city = City.objects.get(name = request.GET['city'])
            pax = request.GET['pax']
            date = request.GET['date']
            property = Property.objects.filter(city = city, maxGuest__gte = pax)

            definitiveProp = []

            for i in property:
                try:
                    property2 =  DateRental.objects.get(property = i, date = datetime.datetime.strptime(date,'%Y-%m-%d').date())
                    definitiveProp.append(property2)
                except:
                    pass

            for indice in range(len(property)):
                property[indice].comision = property[indice].priceDays * 0.08

        except:
            definitiveProp = []
        return render(request, 'show_rooms.html', {'rooms': definitiveProp})
            #date__gt = datetime.datetime.strptime(date1,'%Y-%m-%d').date() less
            #date__gte = datetime.datetime.strptime(date1,'%Y-%m-%d').date() greater

def show_singleR_view(request,room_id):

    if request.method == 'GET':
        try:
            singular_room = DateRental.objects.get(id=room_id)
            return render_to_response('show_single_room.html', {'room': singular_room})
        except:
            return render_to_response('index.html')

    elif request.method == 'POST':
        try:
            guest = Guest(name=request.POST['name'],surename = request.POST['surname'], email = request.POST['email'])
            guest.save()

            code = random.randint(0, 850000000000000)

            property = Property.objects.get(id = request.POST['propertyId'])

            reservation = Reservation(code = code,total = 0, property = property, guest = guest)

            reservation.save()

            date = DateRental.objects.get(property = property, date = request.POST['date'])
            date.reservation = reservation

            date.save()

            return render_to_response('index.html')
        except:
            print 'se rompio todoooooooooooooooooooooooo'
