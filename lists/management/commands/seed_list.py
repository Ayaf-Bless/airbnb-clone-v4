import random
from abc import ABC
from django_seed import Seed
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from lists import models as list_model
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand, ABC):
    help = "this creates many list"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, help="how many lists do you want to create", default=2)

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(list_model.List, number, {
            "user": lambda x: random.choice(users)
        })
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_models = list_model.List.objects.get(pk=pk)
            to_add = rooms[random.randint(1, 7):random.randint(8, 30)]
            list_models.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} lists were created!"))
