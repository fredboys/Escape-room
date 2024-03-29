from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
import datetime


class Room(models.Model):
    """
    Room model
    """
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField()
    image = CloudinaryField('image')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        #  Returns a string of name of escape room
        return f"{self.name}"


class Booking(models.Model):
    """
    Booking model
    """
    user = models.ForeignKey(
        User,
        related_name="user",
        on_delete=models.CASCADE,
        )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    date = models.DateField(null=True)
    time = models.TimeField()
    room_name = models.ForeignKey(
        Room,
        related_name="room_name",
        on_delete=models.PROTECT,
        null=True
        )

    def is_time_taken(self):
        """
        This makes sure the user trying to update the booking,
        is the user that the booking belongs to.
        Also when they update it makes sure they cant double book.
        """
        current_user = None
        if hasattr(self, "user") and self.user is not None:
            current_user = self.user.id

        return Booking.objects\
            .filter(date=self.date)\
            .filter(time=self.time)\
            .filter(room_name=self.room_name)\
            .exclude(user_id=current_user)

    def save(self, *args, **kwargs):
        """
        Gives message if they try to book in the past
        """
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name
