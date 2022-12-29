from django.urls import path
from .views import Home, Rooms, Booking


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('rooms/', Rooms.as_view(), name='room'),
    path('book/', Booking.as_view(), name='book'),
]
