import os

import pymongo

USER = os.environ["DOCUMENTDB_USER"]
PASSWORD = os.environ["DOCUMENTDB_PASSWORD"]
HOST = os.environ["DOCUMENTDB_ENDPOINT"]

client = pymongo.MongoClient(
    f"mongodb://{USER}:{PASSWORD}@{HOST}:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred"
)

db = client.restaurants

db.restaurants.create_index(
    [("address.location", pymongo.ASCENDING), ("updatedAt", pymongo.DESCENDING)]
)

print("Index created successfully.")
