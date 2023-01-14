from .models import Booking, Room
from django import forms
import datetime


class DateInput(forms.DateInput):
    """
    This class gets the widget working to show a datepicker
    """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """
    This class gets the widget working to show a time picker
    """
    input_type = 'text'


class BookingForm(forms.ModelForm):
    """
    This class shows what inputs will be used in the form.
    Also gets the widgets for the time and date working
    """
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
