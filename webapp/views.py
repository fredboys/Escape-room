from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from .models import Room, Booking
from .forms import BookingForm


class Home(generic.TemplateView):

    template_name = 'index.html'


class Rooms(generic.ListView):
    '''
    Display room images, title, descriptions and prices for the website
    '''
    model = Room

    queryset = Room.objects.all()
    template_name = 'room.html'


class Booking(CreateView):
    '''
    After submitting the form user details will be saved in the database
    and users will be redirected to the manage booking page.
    '''
    template_name = 'book.html'
    form_class = BookingForm


