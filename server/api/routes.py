from typing import Optional

from django.http import HttpRequest
from ninja import NinjaAPI

from api.models import Product
from api.schemas import NotFoundSchema, ProductsListResponseSchema

# Create Ninja API instance
app = NinjaAPI()


@app.get("/healthcheck")
def api_healthcheck(request):
    """Check if the API is up and running."""
    return {"status": "ok"}


@app.get("/products", response={200: ProductsListResponseSchema})
def get_products_list(request: HttpRequest, is_featured: Optional[bool] = None):
    """Return a list of all products"""
    products = None
    print("is_featured:", is_featured)

    if is_featured:
        products = Product.objects.filter(is_featured=True)
        return 200, {
            "count": len(list(products)),
            "data": list(products),
        }

    products = Product.objects.all()

    return 200, {
        "count": len(list(products)),
        "data": list(products),
    }


@app.get(
    "/products/{product_id}",
    response={200: ProductsListResponseSchema, 404: NotFoundSchema},
)
def get_product_by_id(request, product_id: str):
    """Return a single product by ID"""
    try:
        product = Product.objects.filter(id=product_id)

        if not product:
            raise Exception("Product not found")
        return 200, {"status": "success", "data": list(product)}
    except Exception as err:
        return 404, {"message": "Product not found"}
