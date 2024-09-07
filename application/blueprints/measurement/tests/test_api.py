# from application.schema import schema
# import pytest
# from schema import schema
# from ..models import Measurement
# from ..repository import MeasurementRepository
from server import app

# from datetime import datetime

# from utilities.pytest.fixtures import db


# Fixture to insert test data into the database
# @pytest.fixture
# async def setup_test_data(db):
#     from datetime import datetime

#     # Insert test data into the database (create MeasurementModel instances)
#     # Ensure the inserted data reflects what your tests expect
#     # You can use the ORM methods to create and insert documents into the database
#     await Measurement.insert_many(
#         [
#             Measurement(weight=5, id="655908cb12f99780df026725", date=datetime.now()),  # Add other necessary fields
#             # Add more MeasurementModel instances as needed
#         ]
#     )


# @pytest.fixture
# def test_cli(event_loop, sanic_client):
#     return event_loop.run_until_complete(sanic_client(app))


# async def test_query_async(monkeypatch):
#     # def mockreturn():
#     #     return {"data": {"measurements": [{"weight": 5.5}]}}

#     # monkeypatch.setattr(
#     #     MeasurementRepository,
#     #     "list",
#     #     mockreturn,
#     # )
#     await Measurement.insert_many(
#         [
#             Measurement(weight=5.5, date=datetime.now()),  # Add other necessary fields
#             # Add more MeasurementModel instances as needed
#         ]
#     )
#     request, response = await app.asgi_client.post(
#         "/graphql",
#         json={
#             "query": """
#                 query {
#                     measurements {
#                         weight
#                     }
#                 }
#             """
#         },
#     )

#     assert response.json == {
#         "data": {
#             "measurements": [
#                 {
#                     "weight": 5,
#                 }
#             ],
#         }
#     }
#     # # await setup_test_data
#     # result = await schema.execute(
#     #     query,
#     #     variable_values={},
#     # )

#     # print(result.errors)
#     # assert result.errors is None
#     # assert result.data["measurements"] == [
#     #     {
#     #         "weight": 5,
#     #     }
#     # ]


async def test_query(measurements):
    await measurements(number=2)

    request, response = await app.asgi_client.post(
        "/graphql",
        json={
            "query": """
                query {
                    measurements {
                        weight
                    }
                }
            """
        },
    )

    assert response.json == {
        "data": {
            "measurements": [
                {
                    "weight": 0.0,
                },
                {
                    "weight": 1.0,
                },
            ],
        }
    }
