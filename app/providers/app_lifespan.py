from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.providers.database import db, objects, redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    # This hook ensures that a connection is opened to handle any queries

    yield

    # This hook ensures that the connection is closed when we've finished processing the request.

    await objects.close()

    if redis_client:
        redis_client.close()
