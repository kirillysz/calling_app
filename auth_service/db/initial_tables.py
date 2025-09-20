from auth_service.db.models.user import User

from auth_service.db.base import Base
from auth_service.db.session import engine

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
