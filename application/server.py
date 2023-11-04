from sanic.response import text
from sanic import Sanic

from utilities.app_factory import create_app


app = create_app()


@app.get("/")
async def hello_workd(request):
    return text("Hello world!")
