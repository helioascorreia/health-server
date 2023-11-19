from pydantic import ValidationError
from datetime import datetime
import strawberry

from utilities.strawberry.utils import clean_input

from .inputs import MeasurementCreateInput, MeasurementUpdateInput
from .types import Measurement
from ..models import Measurement as MeasurementModel


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_measurement(self, input_: MeasurementCreateInput) -> Measurement:
        cleaned_input = clean_input(input_)

        if "date" not in cleaned_input:
            cleaned_input["date"] = datetime.now()

        measurement = MeasurementModel(**cleaned_input)
        instance = await measurement.insert()  # type: ignore
        return Measurement(**instance.model_dump())

    @strawberry.mutation
    async def update_measurement(self, id: strawberry.ID, input_: MeasurementUpdateInput) -> Measurement:
        try:
            instance = await MeasurementModel.get(id)
        except ValidationError as _:
            instance = None

        if instance is None:
            raise Exception("Not found")

        cleaned_input = clean_input(input_)
        await instance.set(cleaned_input)

        return Measurement(**instance.model_dump())

    @strawberry.mutation
    async def delete_measurement(self, id: strawberry.ID) -> bool:
        try:
            instance = await MeasurementModel.get(id)
        except ValidationError as _:
            instance = None

        if instance is None:
            raise Exception("Not found")

        await instance.delete()  # type: ignore
        return True
