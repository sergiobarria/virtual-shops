from django.contrib import admin
from django.urls import path
from products.api import products_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/products/", products_api.urls),
]
