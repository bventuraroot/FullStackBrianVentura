from django.contrib import admin
from .models import Bookings, Courts, Frecuency, States, Partners

admin.site.register([Bookings, Courts, Frecuency, States, Partners])
