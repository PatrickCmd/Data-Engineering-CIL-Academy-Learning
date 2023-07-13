import json
import os

import pymongo

USER = os.environ["DOCUMENTDB_USER"]
PASSWORD = os.environ["DOCUMENTDB_PASSWORD"]
HOST = os.environ["DOCUMENTDB_ENDPOINT"]

client = pymongo.MongoClient(
    f"mongodb://{USER}:{PASSWORD}@{HOST}:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred"
)

db = client.restaurants

with open("scripts/restaurant_1.json", "r") as f:
    restaurant = json.load(f)
    db.restaurants.insert_one(restaurant)

with open("scripts/restaurant_2.json", "r") as f:
    restaurant = json.load(f)
    db.restaurants.insert_one(restaurant)

print("Documents loaded successfully.")

db.restaurants.create_index([("name", pymongo.DESCENDING)])

print("Index created successfully.")
