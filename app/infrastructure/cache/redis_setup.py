from app.infrastructure.cache.redis_client import RedisClient

redis_client: RedisClient | None = None

async def connect_redis():
    global redis_client
    redis_client = RedisClient()


async def close_redis():
    global redis_client
    if redis_client:
        await redis_client.client.close()


def get_redis_client() -> RedisClient:
    if redis_client is None:
        raise RuntimeError("Redis client not initialized")
    return redis_client