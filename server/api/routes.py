from ninja import NinjaAPI

from api.schemas import NotFoundSchema

from .products import products

app = NinjaAPI()


@app.get("/healthcheck")
def api_healthcheck(request):
    """Check if the API is up and running."""
    return {"status": "ok"}


@app.get("/products")
def get_all_products(request):
    """Return a list of all products"""
    return {"data": products}


@app.get("/products/{product_id}")
def get_product_by_id(request, product_id: int):
    """Return a single product by ID"""
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    # if not product:
    #     return 404, {"message": "Product not found"}

    return {"data": product}
    # try:
    #     for p in products:
    #         if p["id"] == product_id:
    #             return {"data": p}
    # except:
    #     return 404, {"message": "Product not found"}
