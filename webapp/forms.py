from .models import Booking, Room
from django import forms
import datetime


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        rooms = Room.objects.filter().order_by("name").values()
        room_tuples = [("", "----------")]
        room_tuples = room_tuples + [(str(
            i["id"]) + "," + str(
                i["duration"]), i["name"] + " - " + "£" + str(i["price"])) for i in rooms]
        self.fields['room_name'] = forms.ChoiceField(choices=room_tuples)


    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email',  'phone',
                  'date', 'time', 'room_name')
