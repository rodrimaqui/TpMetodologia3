from django.shortcuts import render
from Hospedajes.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')