# myapp/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from faker import Faker
from flora.models import Plant, Discoverer
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        amount = 10000
        discoverers = []

        for _ in range(amount):
            discoverer = Discoverer.objects.create(
                first_name = fake.first_name(),
                last_name = fake.last_name()
            )
            discoverers.append(discoverer)

        for _ in range(amount):
            Plant.objects.create(
                name = fake.word(),
                bloom_start=fake.date_this_year(),
                bloom_end=fake.date_this_year(),
                planting_season_start=fake.date_this_year(),
                planting_season_end=fake.date_this_year(),
                discoverer=random.choice(discoverers),
            )
