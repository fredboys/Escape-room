from django.urls import path
from .views import Home, Rooms, Booking, booking


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('rooms/', Rooms.as_view(), name='room'),
    path('book/', booking, name='book'),
]
