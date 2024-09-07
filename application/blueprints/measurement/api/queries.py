from pydantic import ValidationError
import strawberry

from .types import Measurement
from ..models import Measurement as MeasurementModel
from ..repository import MeasurementRepository


@strawberry.type
class Query:
    @strawberry.field
    async def measurements(self) -> list[Measurement]:
        # from datetime import datetime

        # return [
        #     Measurement(
        #         weight=5,
        #         id="1",
        #         date=datetime.now(),
        #         metabolic_age=0,
        #         body_mass_index=0,
        #         body_fat=0,
        #         arm_right_fat=0,
        #         arm_left_fat=0,
        #         leg_right_fat=0,
        #         leg_left_fat=0,
        #         torso_fat=0,
        #         body_muscle=0,
        #         arm_right_muscle=0,
        #         arm_left_muscle=0,
        #         leg_right_muscle=0,
        #         leg_left_muscle=0,
        #         torso_muscle=0,
        #         bone_mass=0,
        #         visceral_fat=0,
        #         body_watter=0,
        #         diary_calorie_intake=0,
        #     )
        # ]

        measurements = await MeasurementModel.find().to_list()
        # measurements = await MeasurementRepository.list()

        return [Measurement(**measurement.model_dump()) for measurement in measurements]

    @strawberry.field
    async def measurement(self, id: str) -> Measurement:
        try:
            instance = await MeasurementModel.get(id)
        except ValidationError as _:
            instance = None

        if instance is None:
            raise Exception("Not found")

        return Measurement(**instance.model_dump())
