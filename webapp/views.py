from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Room


class Home(generic.TemplateView):

    template_name = 'index.html'


class Rooms(generic.ListView):
    '''
    Display treatments images, title, descriptions and prices for the website
    '''
    model = Room

    queryset = Room.objects.all()
    template_name = 'room.html'
