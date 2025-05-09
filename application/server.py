# from sanic.response import text
# from sanic import Sanic
from strawberry.sanic.views import GraphQLView

# from motor.motor_asyncio import AsyncIOMotorClient

# from blueprints.measurement.view import bp as measurement_bp
# from worker.mongo import 

from schema import schema

from utilities.app_factory import create_app

# from beanie import init_beanie

app = create_app(init_blueprints=[
    "blueprints.measurement.view",
    "worker.mongo",
])

# @app.before_server_start
# async def setup_mongo(app, _):
#     app.ctx.mongo_client = AsyncIOMotorClient(app.config.MONGO_URL)
#     await init_beanie(
#         database=app.ctx.mongo_client.health,
#         document_models=[
#             "blueprints.measurement.models.Measurement",
#         ],
#     )


# @app.after_server_stop
# async def shutdown_mongo(app, _):
#     app.ctx.mongo_client.close()


# @app.get("/")
# async def hello_world(request):
#     return text("Hello, world!")


app.add_route(
    GraphQLView.as_view(schema=schema, graphiql=True),
    "/graphql",
)
