from django.shortcuts import render, render_to_response
from models import *
import datetime
from datetime import timedelta
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
                    property2 =  DateRental.objects.get(property = i,date = date)
                    definitiveProp.append(property2)
                except:
                    pass

            for indice in range(len(property)):
                property[indice].comision = property[indice].priceDays * 0.08

        except:
            definitiveProp = []
            print 'SE ROMPIO TOOOODOOOO'
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

            property = Property.objects.get(id=request.POST['propertyId'])



            if dateAble(request.POST['fromD'],request.POST['toD'],property):
                guest = Guest(name=request.POST['name'],surename = request.POST['surname'], email = request.POST['email'])
                guest.save()
                code = random.randint(0, 850000000000000)



                reservation = Reservation(code = code,total = 0, property = property, guest = guest)

                reservation.save()



                saveRangeDate(datetime.datetime.strptime(request.POST['fromD'], "%Y-%m-%d").date(), datetime.datetime.strptime(request.POST['toD'], "%Y-%m-%d").date(), reservation, property)

                print reservation.property.priceDays

                countDays = amount(datetime.datetime.strptime(request.POST['fromD'], "%Y-%m-%d").date(),datetime.datetime.strptime(request.POST['toD'], "%Y-%m-%d").date())

                print countDays

                reservation.total = reservation.property.priceDays * countDays
                reservation.save()


            return render_to_response('details.html')

        except:
            print 'se rompio todoooooooooooooooooooooooo'

def dateAble(fromD,toD,property):
    able = True
    try:
        auxDate = DateRental.objects.filter(date__range=[fromD, toD],property = property)
        for a in auxDate:
            if a.reservation is not None:
                able = False
                break

        return able

    except:
        able = False
        return able

def saveRangeDate(fromD, toD, reservation, property):
    while(fromD <= toD):
        dateRent = DateRental.objects.get(date=fromD,property = property)
        dateRent.reservation = reservation
        dateRent.save()
        fromD = fromD + timedelta(days=1)

def amount(fromD,toD):
    countD = 0
    while(fromD <= toD):
        countD = countD +1
        fromD = fromD + timedelta(days=1)
        print countD
    return countD