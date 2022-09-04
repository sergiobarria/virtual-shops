import json
from random import randint

from api.models import Media, Product
from core.storage_backends import PublicMediaStorage
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

BASE_URL = settings.BASE_DIR / "api" / "data"


class Command(BaseCommand):
    help = "Import products from json file"

    def handle(self, *args, **options) -> None:
        # Set path to the file
        datafile = settings.BASE_DIR / "api" / "data" / "products.json"
        assert datafile.exists(), "File not found"

        # Clean up the products table
        Product.objects.all().delete()

        # load the datafile
        with open(datafile, "r") as f:
            data = json.load(f)

        media_storage = PublicMediaStorage()

        # Save products to the database
        for product in data:
            img_file = product["image"]
            filename = img_file.split("/")[-1]
            del product["image"]

            # Upload image to AWS S3 and save url to db
            with open(BASE_URL / img_file, "rb") as f:
                media_storage.save(filename, f)
                file_url = media_storage.url(filename)
                Media.objects.create(
                    image=file_url, alt_text=f"{product['name']} image"
                )

            product["user"] = User.objects.get(id="1")
            product["image"] = Media.objects.get(image=file_url)
            product["amount"] = randint(1, 100)
            product["ratings_count"] = randint(1, 5000)
            if "is_featured" in product:
                product["is_featured"] = (
                    True if product["is_featured"] == "true" else False
                )

            #  Save product to the database
            Product.objects.create(**product)
