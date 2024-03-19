from django.contrib import admin
from .models import MenuTable,Booking,Users
# Register your models here.
admin.site.register(Users)
admin.site.register(MenuTable)
admin.site.register(Booking)