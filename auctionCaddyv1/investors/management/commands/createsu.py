from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="hakan").exists():
            User.objects.create_superuser("hakan", "hakan@cartertxrealty.com", "cartertxrealty")
            self.stdout.write(self.style.SUCCESS('Successfully created a new super user.'))