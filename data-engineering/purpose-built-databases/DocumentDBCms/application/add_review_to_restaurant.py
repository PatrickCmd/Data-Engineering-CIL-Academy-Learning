import datetime
import os

import pymongo

USER = os.environ["DOCUMENTDB_USER"]
PASSWORD = os.environ["DOCUMENTDB_PASSWORD"]
HOST = os.environ["DOCUMENTDB_ENDPOINT"]

client = pymongo.MongoClient(
    f"mongodb://{USER}:{PASSWORD}@{HOST}:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retrywrites=false"
)

db = client.restaurants


def add_review_to_restaurant(name, review):
    db.restaurants.update_one(
        {"name": name},
        {
            "$push": {"promotedReviews": review},
            "$set": {"updatedAt": datetime.datetime.now().isoformat(),},
        },
    )
    return


add_review_to_restaurant(
    "The Vineyard",
    {
        "reviewer": "elated_eric",
        "rating": 5,
        "review": "Sooo good! Can't wait to come back.",
    },
)
