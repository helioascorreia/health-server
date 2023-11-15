import strawberry
from strawberry.tools import merge_types

from blueprints.measurement.api.queries import Query as MeasurementQuery
from blueprints.measurement.api.mutations import Mutation as MeasurementMutation

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
)
