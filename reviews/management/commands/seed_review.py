import random
from abc import ABC
from django_seed import Seed
from django.core.management.base import BaseCommand
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand, ABC):
    help = "this creates many reviews"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, help="how many users do you want to create", default=2)

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(review_models.Review, number, {
            "accuracy": lambda x: random.randint(0, 6),
            "communication": lambda x: random.randint(0, 6),
            "cleanliness": lambda x: random.randint(0, 6),
            "location": lambda x: random.randint(0, 6),
            "check_in": lambda x: random.randint(0, 6),
            "value": lambda x: random.randint(0, 6),
            "room": lambda x: random.choice(rooms),
            "user": lambda x: random.choice(users)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews were created!"))
