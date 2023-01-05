from .models import Booking, Room
from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'text'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'phone', 'date', 'time', 'room_name')
        widgets = {
            'date': DateInput(attrs={
                'min': datetime.date.today()+datetime.timedelta(days=0),
                'max': datetime.date.today()+datetime.timedelta(days=30)}),
            'time': TimeInput(attrs={
                'class': 'timepicker'}),
        }


class EditBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'phone', 'date', 'time', 'room_name')
        widgets = {
            'date': DateInput(attrs={
                'min': datetime.date.today()+datetime.timedelta(days=0),
                'max': datetime.date.today()+datetime.timedelta(days=30)}),
            'time': TimeInput(attrs={
                'class': 'timepicker'}),
        }