from django.contrib import admin

# Register your models here.

from .models import Guest, Room, Registration

admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Registration)
