from django.core.management.base import BaseCommand
from hotel.models import Guest, Room, Booking

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
     
        guests = [
            {'registration_number': 1, 'last_name': 'Шевченко', 'first_name': 'Тарас', 'middle_name': 'Григорович', 'city': 'Київ'},
            {'registration_number': 2, 'last_name': 'Франко', 'first_name': 'Іван', 'middle_name': 'Якович', 'city': 'Львів'},
         
        ]
        for guest in guests:
            Guest.objects.create(**guest)

        rooms = [
            {'room_number': 101, 'num_rooms': 1, 'floor': 1, 'has_tv': True, 'has_fridge': False, 'num_beds': 2, 'category': 'Standard', 'price_per_night': 100},
            {'room_number': 102, 'num_rooms': 2, 'floor': 1, 'has_tv': True, 'has_fridge': True, 'num_beds': 4, 'category': 'Deluxe', 'price_per_night': 250},
        
        ]
        for room in rooms:
            Room.objects.create(**room)

      
        bookings = [
            {'registration_code': 1, 'guest_id': 1, 'arrival_date': '2024-11-16', 'days_stayed': 3, 'room_number_id': 101},
            {'registration_code': 2, 'guest_id': 2, 'arrival_date': '2024-11-14', 'days_stayed': 2, 'room_number_id': 102},
          
        ]
        for booking in bookings:
            Booking.objects.create(**booking)

        self.stdout.write(self.style.SUCCESS('Database has been populated successfully!'))
