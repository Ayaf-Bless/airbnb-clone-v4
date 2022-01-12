from abc import ABC

from django.core.management.base import BaseCommand


class Command(BaseCommand, ABC):
    help = "this tell me anything"

    def add_arguments(self, parser):
        parser.add_argument("--times", help="how many times should repeat")

    def handle(self, *args, **options):
        time = int(options.get("times"))
        for t in range(0, time):
            self.stdout.write(self.style.ERROR("I love you"))
