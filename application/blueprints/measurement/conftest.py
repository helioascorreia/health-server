# import motor.motor_asyncio
# from motor.motor_asyncio import AsyncIOMotorClient
import pytest
from random import randint

# from pydantic_settings import BaseSettings
from beanie import init_beanie
from .models import Measurement
from typing import List
from datetime import datetime


@pytest.fixture(autouse=True)
async def init(db):
    models = [
        Measurement,
    ]
    await init_beanie(
        database=db,
        document_models=models,
    )

    yield None

    for model in models:
        await model.get_motor_collection().drop()
        await model.get_motor_collection().drop_indexes()


@pytest.fixture
def measurements_not_inserted():
    def generate_measurements(number: int, random: bool = False) -> List[Measurement]:
        return [
            Measurement(
                date=datetime.now(),
                weight=randint(0, 100) if random else i,
            )
            for i in range(number)
        ]

    return generate_measurements


@pytest.fixture
def measurements(measurements_not_inserted):
    async def generate_measurements(number: int, random: bool = False):
        result = await Measurement.insert_many(measurements_not_inserted(number, random))
        return result.inserted_ids

    return generate_measurements
