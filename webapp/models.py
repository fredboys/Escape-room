from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from users.models import User
import datetime


class Room(models.Model):
    """
    Room model
    """
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
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
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = PhoneNumberField()
    date = models.DateField(null=True)
    time = models.TimeField(default=datetime.time(12, 00))

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Booking, self).save(*args, **kwargs)
