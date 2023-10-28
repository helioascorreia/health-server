from sanic import Sanic
from sanic.response import text


app = Sanic("Health")


@app.get("/")
async def hello_workd(request):
    return text("Hello world!")
