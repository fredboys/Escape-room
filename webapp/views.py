from django.shortcuts import render, redirect
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


def booking(request):
    form = BookingForm()
    booked = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            booked = True

    context = {
        'form': form,
        'booked': booked,
        }
    
    return render(request, 'book.html', context)


def account(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }

    return render(request, 'my_booking.html', context)


def update_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    form = BookingForm(instance=booking)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        'form': form,
    }

    return render(request, 'edit_book.html', context)


def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    return redirect('account')

