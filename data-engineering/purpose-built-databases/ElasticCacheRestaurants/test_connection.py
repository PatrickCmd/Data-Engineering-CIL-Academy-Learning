import os

import redis

HOST = os.environ["REDIS_HOSTNAME"].replace(":6379", "")

r = redis.Redis(host=HOST)

r.ping()

print("Connected to Redis!")
