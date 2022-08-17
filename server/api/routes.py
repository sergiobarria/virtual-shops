from ninja import NinjaAPI

app = NinjaAPI()


@app.get("/healthcheck")
def api_healthcheck(request):
    return {"status": "ok"}
