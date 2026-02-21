from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.players import router as players_router
from app.infrastructure.cache.redis_setup import connect_redis, close_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_redis()
    yield
    await close_redis()

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(players_router)
