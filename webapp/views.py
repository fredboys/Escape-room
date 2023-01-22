from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from .models import Room, Booking
from .forms import BookingForm


class Home(generic.TemplateView):
    """
    View to dispaly the Homepage including Hero image, about us
    """
    template_name = 'index.html'


class Rooms(generic.ListView):
    '''
    Display room images, title, descriptions and prices for the website
    '''
    model = Room

    queryset = Room.objects.all()
    template_name = 'room.html'


def booking(request):
    """
    To display the booking form so the user can book a room.
    They get a message if their enetered booking has already been booked.
    They get an email for confirmation.
    """
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
                email_to = booking.email
                subject = 'Your booking'
                message = f'Hi {booking.first_name}, your booking on\
                        {booking.date} for {booking.room_name}\
                        at {booking.time} has been placed.\
                        We look forward to seeing you!'
                email_from = 'theescaperoomldn@gmail.com'
                recipient_list = [email_to, ]
                send_mail(subject, message, email_from, recipient_list)
            else:
                error = "This slot is not available"

    context = {
        'form': form,
        'booked': booked,
        "error": error
        }

    return render(request, 'book.html', context)


def account(request):
    """
    View to display the users booking page
    """
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }

    return render(request, 'my_booking.html', context)


def update_booking(request, booking_id):
    """
    Allows the user to update their booking.
    Also restricts the users to only update their booking.
    Also get an email confirmation.
    """
    booking = Booking.objects.get(id=booking_id)
    is_authenticated = request.user.is_authenticated and booking.user.id == request.user.id
    if is_authenticated:
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
                        {booking.date} for {booking.room_name}\
                        at {booking.time} has been updated.\
                        We look forward to seeing you!'
                    email_from = 'theescaperoomldn@gmail.com'
                    recipient_list = [email_to, ]
                    send_mail(subject, message, email_from, recipient_list)
                    messages.success(request, 'Updated successfully!')
                    return redirect('account')
                else:
                    error_message = "That slot is not available"
    else:
        return render(request, '500.html')

    context = {
        'form': form,
        'is_authenticated': is_authenticated,
        "error": error_message
    }

    return render(request, 'edit_book.html', context)


def delete_booking(request, booking_id):
    """
    Allows the user to delete their booking
    and sends email confirmation.
    """
    booking = Booking.objects.get(id=booking_id)
    is_authenticated = request.user.is_authenticated and booking.user.id == request.user.id
    if is_authenticated:
        booking.delete()
        email_to = booking.email
        subject = 'Your booking'
        message = f'Hi {booking.first_name}, your booking on\
                {booking.date} for {booking.room_name}\
                at {booking.time} has been cancelled.\
                We hope to see you soon'
        email_from = 'theescaperoomldn@gmail.com'
        recipient_list = [email_to, ]
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Cancellation successfully!')
        return redirect('account')
    else:
        return render(request, '500.html')


def error_404_view(request, exception):
    """
    Displays 404.html path
    """

    return render(request, '404.html')


def handler500(request, *args, **argv):
    return render(request, '500.html')
    