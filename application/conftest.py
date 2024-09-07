import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import pytest
from pydantic_settings import BaseSettings
from beanie import init_beanie
from blueprints.measurement.models import Measurement


class Settings(BaseSettings):
    mongodb_dsn: str = "mongodb://root:rootpassword@mongo:27017/health-test?authSource=admin"
    mongodb_db_name: str = "health-test"


@pytest.fixture
def settings():
    return Settings()


@pytest.fixture()
def cli(settings):
    return motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_dsn)


@pytest.fixture()
def db(cli, settings):
    return cli[settings.mongodb_db_name]


# @pytest.fixture()
# async def init(db):
#     models = [
#         Measurement,
#     ]
#     await init_beanie(
#         database=db,
#         document_models=models,
#     )
#     print("*" * 30)
#     yield None

#     for model in models:
#         await model.get_motor_collection().drop()
#         await model.get_motor_collection().drop_indexes()
