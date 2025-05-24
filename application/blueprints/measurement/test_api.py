from sanic import Sanic

from .models import Measurement
from datetime import datetime


def test_sample(app: Sanic):
    request, response = app.test_client.get("/graphql")
    assert response.status == 200


def test_not_found(app: Sanic):
    request, response = app.test_client.get("/")
    assert response.status == 404


async def test_query(test_client):
    query = """
        query {
            measurements {
                weight
            }
        }
    """

    await test_client.sanic_app.ctx.mongo_db.measurements.insert_one(
        Measurement(date=datetime.now(), weight=70.5).model_dump()
    )

    _, response = await test_client.post("/graphql", json={"query": query})
    response_json = response.json
    
    assert response_json["data"]["measurements"] == [
        {"weight": 70.5},
    ]
  