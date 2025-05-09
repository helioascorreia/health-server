from pydantic import ValidationError
import strawberry
from bson.objectid import ObjectId

from .types import Measurement
from ..models import Measurement as MeasurementModel


@strawberry.type
class Query:
    @strawberry.field
    async def measurements(self, info) -> list[Measurement]:
        db = info.context["request"].app.ctx.mongo_db
        cursor = db.measurement.find()
        measurements = [MeasurementModel(**measurement) for measurement in await cursor.to_list(length=100)]
        return [Measurement(**measurement.model_dump()) for measurement in measurements]

    @strawberry.field
    async def measurement(self, info, id_: str) -> Measurement:
        db = info.context["request"].app.ctx.mongo_db
        try:
            instance = await db.measurement.find_one({"_id": ObjectId(id_)})
        except ValidationError as _:
            instance = None

        if instance is None:
            raise Exception("Not found")

        return Measurement(**MeasurementModel(**instance).model_dump())
