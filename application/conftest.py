import pytest
import pymongo
import os
from sanic_testing.testing import SanicASGITestClient

from server import app as application_instance
from utilities.app_factory import create_app

from strawberry.sanic.views import GraphQLView
from schema import schema


@pytest.fixture
def app():
    return application_instance


# @pytest.fixture
# async def test_client(monkeypatch):
#     monkeypatch.setenv(
#         "SANIC_MONGO_URL",
#         "mongodb://root:rootpassword@mongo-testing:27017", 
#     )
#     return SanicASGITestClient(application_instance)

@pytest.fixture
async def test_client(monkeypatch):
    monkeypatch.setenv(
        "SANIC_MONGO_URL",
        "mongodb://root:rootpassword@mongo-testing:27017", 
    )
    app = create_app(init_blueprints=[
        "blueprints.measurement.view",
        "worker.mongo",
    ])
    app.add_route(
        GraphQLView.as_view(schema=schema, graphql_ide=True),
        "/graphql",
    )
    return SanicASGITestClient(app)