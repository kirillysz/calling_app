from fastapi import FastAPI
from program_service.routes.program import router as program_router

from contextlib import asynccontextmanager
from program_service.db.init_tables import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(program_router)