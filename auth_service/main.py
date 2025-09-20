from fastapi import FastAPI
from auth_service.routes.auth import router as auth_router

from contextlib import asynccontextmanager
from auth_service.db.initial_tables import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)