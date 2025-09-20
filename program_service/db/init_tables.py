from program_service.db.models.program import Program

from program_service.db.base import Base
from program_service.db.session import engine

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
