from sanic import Sanic
from pymongo import AsyncMongoClient


app = Sanic.get_app()


@app.before_server_start
async def setup_mongo(app, _):
    app.ctx.mongo_client = AsyncMongoClient(app.config.MONGO_URL)
    app.ctx.mongo_db = app.ctx.mongo_client.health


@app.after_server_stop
async def shutdown_mongo(app, _):
    await app.ctx.mongo_client.close()
