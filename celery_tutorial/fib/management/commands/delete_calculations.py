from django.core.management.base import BaseCommand
from fib.models import Calculation

class Command(BaseCommand):
    def handle(self, *args, **options):
        Calculation.objects.all().delete()
