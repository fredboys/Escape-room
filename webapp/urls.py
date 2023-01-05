from django.urls import path
from .views import Home, Rooms, booking, account, update_booking, delete_booking


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('rooms/', Rooms.as_view(), name='room'),
    path('book/', booking, name='book'),
    path('my_account/', account, name='account'),
    path('update_booking/<int:booking_id>/', update_booking, name='update'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete')
]
