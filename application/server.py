from strawberry.sanic.views import GraphQLView
from schema import schema

from utilities.app_factory import create_app


app = create_app(init_blueprints=[
    "blueprints.measurement.view",
    "worker.mongo",
])

app.add_route(
    GraphQLView.as_view(schema=schema, graphql_ide=True),
    "/graphql",
)
