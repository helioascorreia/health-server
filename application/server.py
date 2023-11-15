from sanic.response import text
from sanic import Sanic
from strawberry.sanic.views import GraphQLView

from schema import schema

from utilities.app_factory import create_app


app = create_app()


app.add_route(
    GraphQLView.as_view(schema=schema, graphiql=True),
    "/graphql",
)
