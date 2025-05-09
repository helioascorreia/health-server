import strawberry
from typing import Optional
from datetime import datetime


@strawberry.input
class MeasurementInput:
    date: Optional[datetime] = strawberry.UNSET

    metabolic_age: Optional[int] = strawberry.UNSET

    body_mass_index: Optional[float] = strawberry.UNSET  # BMI

    body_fat: Optional[float] = strawberry.UNSET
    arm_right_fat: Optional[float] = strawberry.UNSET
    arm_left_fat: Optional[float] = strawberry.UNSET
    leg_right_fat: Optional[float] = strawberry.UNSET
    leg_left_fat: Optional[float] = strawberry.UNSET
    torso_fat: Optional[float] = strawberry.UNSET

    body_muscle: Optional[float] = strawberry.UNSET
    arm_right_muscle: Optional[float] = strawberry.UNSET
    arm_left_muscle: Optional[float] = strawberry.UNSET
    leg_right_muscle: Optional[float] = strawberry.UNSET
    leg_left_muscle: Optional[float] = strawberry.UNSET
    torso_muscle: Optional[float] = strawberry.UNSET

    bone_mass: Optional[float] = strawberry.UNSET

    visceral_fat: Optional[int] = strawberry.UNSET
    body_watter: Optional[float] = strawberry.UNSET
    diary_calorie_intake: Optional[int] = strawberry.UNSET


@strawberry.input
class MeasurementCreateInput(MeasurementInput):
    weight: float


@strawberry.input
class MeasurementUpdateInput(MeasurementInput):
    id: strawberry.ID
    weight: Optional[float] = strawberry.UNSET
