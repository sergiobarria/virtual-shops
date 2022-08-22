import uuid

from django.contrib.auth.models import User
from django.db import models


class Media(models.Model):
    """Describes the properties of a media file"""

    class Meta:
        db_table = "api_product_image"
        verbose_name_plural = "Media"

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    image = models.FileField(
        max_length=1000,
        null=True,
        blank=True,
    )
    alt_text = models.CharField(max_length=200, blank=True, null=True)

    # Detault properties
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.image)


class Product(models.Model):
    """Describes the properties of a product"""

    class Meta:
        db_table = "api_product"

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(Media, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    amount = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    rating = models.DecimalField(
        max_digits=7, decimal_places=1, default=0, null=True, blank=True
    )
    ratings_count = models.IntegerField(default=0)
    # Detault properties
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    class Meta:
        db_table = "api_review"

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    comment = models.TextField(null=True, blank=True)
    # Detault properties
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.rating)


class Order(models.Model):
    class Meta:
        db_table = "api_order"

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    tax_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    # Detault properties
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.created_at)


class OrderItem(models.Model):
    class Meta:
        db_table = "api_order_item"

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(default=0, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)


class ShippingAddress(models.Model):
    class Meta:
        db_table = "api_shipping_address"

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shipping_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    # Detault properties
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.address
