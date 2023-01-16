from django.contrib import admin
from .models import Room, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'capacity', 'duration')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_filter = ('first_name', 'last_name', 'email')
    list_display = ['date', 'time', 'room_name', 'first_name', 'last_name',
                    'email']
    search_fields = ['first_name']

    @admin.display(description="Room")
    def get_room_name(self, obj):
        return obj.room_name.name
