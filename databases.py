import redis
from functools import lru_cache

@lru_cache(maxsize=1)
def redis_client():
    pool = redis.ConnectionPool.from_url('redis://localhost:6379/0')
    return redis.Redis(connection_pool=pool)
