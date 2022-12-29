from .models import Booking
from django import forms
import datetime


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email',  'phone',
                  'date', 'time', 'room_name')
