from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail
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
    error = None
    if request.method == 'POST':
        form = BookingForm(request.POST)
        booking = form.save(commit=False)
        if form.is_valid():
            if not booking.is_time_taken():
                booking.user = request.user
                booking.save()
                booked = True
            else:
                error = "This slot is not available"
            email_to = booking.email
            subject = 'Your booking'
            message = f'Hi {booking.first_name}, your booking on\
                    {booking.date} has been placed.\
                    We look forward to seeing you!'
            email_from = 'theescaperoomldn@gmail.com'
            recipient_list = [email_to, ]
            send_mail(subject, message, email_from, recipient_list)

    context = {
        'form': form,
        'booked': booked,
        "error": error
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
    is_authenticated = request.user.is_authenticated and booking.user.id == request.user.id
    error_message = None
    form = BookingForm(instance=booking)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            if not booking.is_time_taken():
                error_message = None
                form.save()
                email_to = booking.email
                subject = 'Your booking'
                message = f'Hi {booking.first_name}, your booking on\
                    {booking.date} has been updated.'
                email_from = 'theescaperoomldn@gmail.com'
                recipient_list = [email_to, ]
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, 'Updated successfully!')
                return redirect('account')
            else:
                error_message = "That slot is not available"

    context = {
        'form': form,
        'is_authenticated': is_authenticated,
        "error": error_message
    }

    return render(request, 'edit_book.html', context)


def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    email_to = booking.email
    subject = 'Your booking'
    message = f'Hi {booking.first_name}, your booking on\
            {booking.date} has been deleted.'
    email_from = 'theescaperoomldn@gmail.com'
    recipient_list = [email_to, ]
    send_mail(subject, message, email_from, recipient_list)
    messages.success(request, 'Cancellation successfully!')
    return redirect('account')
