from api.models import Media, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Deletes all products from the database"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Media.objects.all().delete()
        self.stdout.write(
            self.style.WARNING("Successfully deleted all products and images")
        )
