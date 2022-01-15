import random
from abc import ABC
from django_seed import Seed
from django.core.management.base import BaseCommand
from reservations import models as reservations_models
from users import models as user_models
from rooms import models as room_models
from datetime import timedelta, datetime


class Command(BaseCommand, ABC):
    help = "this creates many reservation"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, help="how many reservation do you want to create", default=2)

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(reservations_models.Reservation, number, {
            "room": lambda x: random.choice(rooms),
            "guest": lambda x: random.choice(users),
            "check_in": lambda x: datetime.now(),
            "check_out": lambda x: datetime.now() + timedelta(days=random.randint(3, 25)),
            "status": lambda x: random.choice(["pending", "confirmed", "canceled"])
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservation were created!"))
