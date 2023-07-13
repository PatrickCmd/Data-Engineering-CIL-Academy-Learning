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


def get_recently_updated_by_location(location):
    results = db.restaurants.find({"address.location": location}).sort(
        [("updatedAt", pymongo.DESCENDING)]
    )
    return results


results = get_recently_updated_by_location("New York, NY")
for restaurant in results:
    print(f"Restaurant: {restaurant['name']}. Updated at {restaurant['updatedAt']}")
