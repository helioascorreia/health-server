from sanic import Sanic
from pymongo import MongoClient
from schema import schema
import os

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
    db = MongoClient("mongodb://root:rootpassword@mongo-testing:27017")["health_test"]
    db.measurements.insert_one({"id": "abc123", "weight": 70.5})

    _, response = await test_client.post("/graphql", json={"query": query})
    response_json = response.json
    
    # assert response.errors is None
    assert response_json["data"]["measurements"] == [
        {"weight": 81},
        {"weight": 80},
    ]
  