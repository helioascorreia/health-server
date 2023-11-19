import strawberry
from strawberry.schema.config import StrawberryConfig
from strawberry.tools import merge_types

from blueprints.measurement.api.queries import Query as MeasurementQuery
from blueprints.measurement.api.mutations import Mutation as MeasurementMutation

from utilities.strawberry.converters import PythonConverter


Query = merge_types(
    "Query",
    (MeasurementQuery,),
)

Mutation = merge_types(
    "Mutation",
    (MeasurementMutation,),
)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(name_converter=PythonConverter()),
)
