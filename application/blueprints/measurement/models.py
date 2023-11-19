from typing import Optional
from datetime import datetime
from beanie import Document


class Measurement(Document):
    date: datetime
    weight: float

    metabolic_age: Optional[int] = None

    body_mass_index: Optional[float] = None  # BMI

    body_fat: Optional[float] = None
    arm_right_fat: Optional[float] = None
    arm_left_fat: Optional[float] = None
    leg_right_fat: Optional[float] = None
    leg_left_fat: Optional[float] = None
    torso_fat: Optional[float] = None

    body_muscle: Optional[float] = None
    arm_right_muscle: Optional[float] = None
    arm_left_muscle: Optional[float] = None
    leg_right_muscle: Optional[float] = None
    leg_left_muscle: Optional[float] = None
    torso_muscle: Optional[float] = None

    bone_mass: Optional[float] = None

    visceral_fat: Optional[int] = None
    body_watter: Optional[float] = None
    diary_calorie_intake: Optional[int] = None

    class Settings:
        name = "measurement"
