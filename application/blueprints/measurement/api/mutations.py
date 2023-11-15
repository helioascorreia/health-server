import strawberry

from .types import Measurement
from ..models import Measurement as MeasurementModel


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_measurement(self, weight: float) -> Measurement:
        measurement = MeasurementModel(weight=weight)
        instance = await measurement.insert()  # type: ignore
        return Measurement(**instance.model_dump())

    @strawberry.mutation
    async def update_measurement(self, id: str, weight: float) -> Measurement:
        instance = await MeasurementModel.get(id)

        if instance is None:
            raise Exception("Not found")

        await instance.set({"weight": weight})

        return Measurement(**instance.model_dump())

    @strawberry.mutation
    async def delete_measurement(self, id: str) -> bool:
        instance = await MeasurementModel.get(id)

        if instance is None:
            raise Exception("Not found")

        await instance.delete()  # type: ignore
        return True
