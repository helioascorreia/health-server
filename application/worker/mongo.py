from sanic import Sanic
import motor.motor_asyncio

app = Sanic.get_app("app")


@app.before_server_start
async def setup_mongo(app, _):
    app.ctx.mongo_client = motor.motor_asyncio.AsyncIOMotorClient(app.config.MONGO_URL)
    app.ctx.mongo_db = app.ctx.mongo_client.health


@app.after_server_stop
async def shutdown_mongo(app, _):
    app.ctx.mongo_client.close()
