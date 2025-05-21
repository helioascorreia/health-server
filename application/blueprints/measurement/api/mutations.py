from pydantic import ValidationError
from datetime import datetime
from bson.objectid import ObjectId
import strawberry

from utilities.strawberry.utils import clean_input

from .inputs import MeasurementCreateInput, MeasurementUpdateInput
from .types import Measurement
from ..models import Measurement as MeasurementModel


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_measurement(self, info: strawberry.Info, input_: MeasurementCreateInput) -> Measurement:
        db = info.context["request"].app.ctx.mongo_db
        cleaned_input = clean_input(input_)

        if "date" not in cleaned_input:
            cleaned_input["date"] = datetime.now()

        measurement = MeasurementModel(**cleaned_input)
        instance = await db.measurement.insert_one(measurement.model_dump())

        created_measurement = await db.measurement.find_one({"_id": instance.inserted_id})
        return Measurement(**MeasurementModel(**created_measurement).model_dump())

    @strawberry.mutation
    async def update_measurement(self, info: strawberry.Info, input_: MeasurementUpdateInput) -> Measurement:
        db = info.context["request"].app.ctx.mongo_db
        cleaned_input = clean_input(input_)
        id_ = cleaned_input.pop("id")

        try:
            instance = MeasurementModel(**await db.measurement.find_one({"_id": ObjectId(id_)}))
        except ValidationError as _:
            instance = None

        if instance is None:
            raise Exception("Not found")

        await db.measurement.update_one({"_id": ObjectId(id_)}, {"$set": cleaned_input})
        updated_measurement = await db.measurement.find_one({"_id": ObjectId(id_)})
        return Measurement(**MeasurementModel(**updated_measurement).model_dump())

    @strawberry.mutation
    async def delete_measurement(self, info: strawberry.Info, id_: strawberry.ID) -> bool:
        db = info.context["request"].app.ctx.mongo_db

        deleted_instance = await db.measurement.delete_one({"_id": ObjectId(id_)})

        if deleted_instance.deleted_count != 1:
            raise Exception("Not found")

        return True
