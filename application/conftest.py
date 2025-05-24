import pytest

from sanic_testing.testing import SanicASGITestClient
from pymongo import AsyncMongoClient

from server import app as application_instance
from utilities.app_factory import create_app

from strawberry.sanic.views import GraphQLView
from schema import schema

from blueprints.measurement.models import Measurement
from datetime import datetime


@pytest.fixture
def app():
    return application_instance



@pytest.fixture
async def test_client():
    app = create_app(init_blueprints=[
        "blueprints.measurement.view",
        # "worker.mongo",
    ])
    app.add_route(
        GraphQLView.as_view(schema=schema, graphql_ide=True),
        "/graphql",
    )

    async def setup_mongo(app, _):
        app.ctx.mongo_client = AsyncMongoClient("mongodb://root:rootpassword@mongo-testing:27017")
        app.ctx.mongo_db = app.ctx.mongo_client.health
        
        # await app.ctx.mongo_db.measurement.insert_one(Measurement(date=datetime.now(), weight=70.5).model_dump())

    async def shutdown_mongo(app, _):
        await app.ctx.mongo_client.drop_database("health")
        await app.ctx.mongo_client.close()


    app.register_listener(setup_mongo, "before_server_start")
    app.register_listener(shutdown_mongo, "after_server_stop")

    return SanicASGITestClient(app)