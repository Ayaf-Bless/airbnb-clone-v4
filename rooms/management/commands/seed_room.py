from abc import ABC
import random

from django_seed import Seed
from django.core.management.base import BaseCommand
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand, ABC):
    help = "this creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, help="how many users do you want to create", default=2)

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get("number")
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(room_models.Room, number, {
            "host": lambda x: random.choice(all_users),
            "room_type": lambda x: random.choice(room_types),
            "price": lambda x: random.randint(1, 300),
            "beds": lambda x: random.randint(1, 5),
            "baths": lambda x: random.randint(1, 5),
            "guests": lambda x: random.randint(1, 19),
            "bedrooms": lambda x: random.randint(1, 5),
            "name": lambda x: seeder.faker.address()
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms were created!"))
