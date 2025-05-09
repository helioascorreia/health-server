from motor.motor_asyncio import AsyncIOMotorClient
import pytest
from sanic import Sanic

@pytest.fixture
def app():
    sanic_app = Sanic("TestSanic")

    return sanic_app

@pytest.fixture
async def db(app):
    if not hasattr(app.ctx, "mongo_client"):
        app.ctx.mongo_client = AsyncIOMotorClient(
            "mongodb://root:rootpassword@mongo:27017/health-test?authSource=admin"
        )

    yield app.ctx.mongo_client["health-test"]

# End of working example

# import pytest
# from motor.motor_asyncio import AsyncIOMotorClient
# from beanie import init_beanie
# from blueprints.measurement.models import Measurement
# import asyncio
# from mongomock_motor import AsyncMongoMockClient

# MONGO_TEST_URL = "mongodb://root:rootpassword@mongo:27017"
# TEST_DB_NAME = "health-test"

# @pytest.fixture()
# async def my_fixture():
#     client = AsyncMongoMockClient()
#     await init_beanie(document_models=[Measurement], database=client.get_database(name="db"))

# @pytest.fixture(scope="session")
# def event_loop():
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()

# @pytest.fixture()
# async def db():
#     client = AsyncIOMotorClient(MONGO_TEST_URL)
#     db = client[TEST_DB_NAME]

#     await init_beanie(database=db, document_models=["blueprints.measurement.models.Measurement",])

#     yield db

#     await client.drop_database(TEST_DB_NAME)


# End of example with beanie that i'm trying to run it successfully

# @pytest.fixture
# async def client():
#     async with app.asgi_client as client:
#         yield client

# @pytest.fixture
# async def mongo_client(client):
#     yield app.ctx.mongo_client
#     # async with app.asgi_client as client:




# class Settings(BaseSettings):
#     mongodb_dsn: str = "mongodb://root:rootpassword@mongo:27017/health-test?authSource=admin"
#     mongodb_db_name: str = "health-test"


# @pytest.fixture
# def settings():
#     return Settings()


# @pytest.fixture()
# def cli(settings):
#     return motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_dsn)


# @pytest.fixture()
# def db(cli, settings):
#     return cli[settings.mongodb_db_name]


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
