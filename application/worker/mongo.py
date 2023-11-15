from sanic import Sanic
from motor.motor_asyncio import AsyncIOMotorClient

from beanie import init_beanie


app = Sanic.get_app("app")


@app.before_server_start
async def setup_mongo(app, _):
    app.ctx.mongo_client = AsyncIOMotorClient(app.config.MONGO_URL)

    await init_beanie(
        database=app.ctx.mongo_client.health,
        document_models=[
            "blueprints.measurement.models.Measurement",
        ],
    )


@app.after_server_stop
async def shutdown_mongo(app, _):
    app.ctx.mongo_client.close()
