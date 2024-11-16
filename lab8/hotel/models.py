from django.db import models



class Guest(models.Model):
    registration_number = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)

class Room(models.Model):
    room_number = models.AutoField(primary_key=True)
    num_of_rooms = models.IntegerField()
    floor = models.IntegerField()
    tv = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    num_of_beds = models.IntegerField()
    category = models.CharField(max_length=50, choices=[
        ('standard', 'Standard'),
        ('semi-lux', 'Semi-lux'),
        ('lux', 'Lux')
    ])
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)

class Booking(models.Model):
    booking_code = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    num_of_days = models.IntegerField()

class Registration(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"