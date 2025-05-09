from sanic import Sanic
from motor.motor_asyncio import AsyncIOMotorClient


app = Sanic.get_app()


@app.before_server_start
async def setup_mongo(app, _):
    app.ctx.mongo_client = AsyncIOMotorClient(app.config.MONGO_URL)
    app.ctx.mongo_db = app.ctx.mongo_client.health

    # if "pytest" in sys.argv[0]:
    #     app.ctx.mongo_client = AsyncIOMotorClient(
    #         "mongodb://root:rootpassword@mongo:27017/health-test?authSource=admin"
    #     )
    # else:
    #     app.ctx.mongo_client = AsyncIOMotorClient(app.config.MONGO_URL)


@app.after_server_stop
async def shutdown_mongo(app, _):
    app.ctx.mongo_client.close()
