import os
from redislite import Redis

db_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

_redis_connection = Redis(f"/{db_path}/redis.db")

def get_redis_connection():
    return _redis_connection