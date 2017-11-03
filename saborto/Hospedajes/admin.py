from django.contrib import admin
from Hospedajes.models import *

class AdminCity(admin.ModelAdmin):
    search_fields = ['name']

class AdminPropery(admin.ModelAdmin):
    search_fields = ['numberCard']
    list_filter = ('numberCard',)
    ordering = ('title',)

# Register your models here.

admin.site.register(City, AdminCity)
admin.site.register(DateRental)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Property,AdminPropery)


