from ninja import NinjaAPI

products_api = NinjaAPI()


@products_api.get("/healthcheck")
def api_healthcheck(request):
    return {"app": "products", "status": "ok"}
