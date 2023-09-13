from django.core.management.base import BaseCommand
from peopleAPI.models import Person

class Command(BaseCommand):
    help = 'Reset auto-increment value for the Person model table.'

    def handle(self, *args, **options):
        # Reset the auto-increment value to 1
        Person.objects.raw("DELETE FROM sqlite_sequence WHERE name = 'peopleAPI_person'")
        self.stdout.write(self.style.SUCCESS('Auto-increment value reset for the Person model table.'))
