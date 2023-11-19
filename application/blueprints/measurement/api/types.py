from typing import Optional
from datetime import datetime

import strawberry


@strawberry.type
class Measurement:
    id: str
    date: datetime
    weight: float

    metabolic_age: Optional[int]

    body_mass_index: Optional[float]  # BMI

    body_fat: Optional[float]
    arm_right_fat: Optional[float]
    arm_left_fat: Optional[float]
    leg_right_fat: Optional[float]
    leg_left_fat: Optional[float]
    torso_fat: Optional[float]

    body_muscle: Optional[float]
    arm_right_muscle: Optional[float]
    arm_left_muscle: Optional[float]
    leg_right_muscle: Optional[float]
    leg_left_muscle: Optional[float]
    torso_muscle: Optional[float]

    bone_mass: Optional[float]

    visceral_fat: Optional[int]
    body_watter: Optional[float]
    diary_calorie_intake: Optional[int]
