from django.urls import path
from .views import Home, Rooms


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('rooms/', Rooms.as_view(), name='room'),
]
