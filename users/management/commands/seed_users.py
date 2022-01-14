from abc import ABC
from django_seed import Seed
from django.core.management.base import BaseCommand
from users import models as user_models


class Command(BaseCommand, ABC):
    help = "this creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number",type=int, help="how many users do you want to create", default=2)

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get("number")
        seeder.add_entity(user_models.User, number, {
            "is_staff": False, "is_superuser": False
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users were created!"))
