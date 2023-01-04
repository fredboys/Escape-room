from django.urls import path
from .views import Home, Rooms, booking, Account


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('rooms/', Rooms.as_view(), name='room'),
    path('book/', booking, name='book'),
    path('my_account/', Account.as_view(), name='account'),
]
