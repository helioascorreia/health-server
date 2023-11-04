from datetime import datetime

from pydantic import BaseModel


class Measurement(BaseModel):
    # id: int
    date_time: datetime
    weight: float
    metabolic_age: int

    body_mass_index: float  # BMI

    body_fat: float
    arm_right_fat: float
    arm_left_fat: float
    leg_right_fat: float
    leg_left_fat: float
    torso_fat: float

    body_muscle: float
    arm_right_muscle: float
    arm_left_muscle: float
    leg_right_muscle: float
    leg_left_muscle: float
    torso_muscle: float

    bone_mass: float

    visceral_fat: int
    body_watter: float
    diary_calorie_intake: int
