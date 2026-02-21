import redis.asyncio


class RedisClient:

    def __init__(self, url: str = "redis://localhost:6379"):
        self.client = redis.asyncio.from_url(url, decode_responses=True)

    async def set(self, key: str, value: str, ttl: int | None = None, **kwargs):
        await self.client.set(name=key, value=value, ex=ttl, **kwargs)

    async def pipeline(self):
        return self.client.pipeline()

    async def get(self, key: str):
        return await self.client.get(key)

    async def delete(self, key: str):
        await self.client.delete(key)

    async def zadd(self, name: str, mapping: dict):
        await self.client.zadd(name, mapping)

    async def zrevrange(self, name: str, start: int, end: int):
        return await self.client.zrevrange(name, start, end)

    async def mget(self, keys: list):
        if not keys:
            return []
        return await self.client.mget(keys)
