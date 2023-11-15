import strawberry

from .types import Measurement
from ..models import Measurement as MeasurementModel


@strawberry.type
class Query:
    @strawberry.field
    async def measurements(self) -> list[Measurement]:
        measurements = await MeasurementModel.find().to_list()

        return [Measurement(**measurement.model_dump()) for measurement in measurements]

    @strawberry.field
    async def measurement(self, id: str) -> Measurement:
        instance = await MeasurementModel.get(id)

        if instance is None:
            raise Exception("Not found")

        return Measurement(**instance.model_dump())
