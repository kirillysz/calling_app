from sqlalchemy.ext.asyncio import AsyncSession

from auth_service.services.jwt import decrypt_token

from program_service.db.models.program import Program
from program_service.schemas.program import ProgramCreate, ProgramBase

class ProgramCrud:
    @staticmethod
    async def create_program(
        db: AsyncSession,
        program_data: ProgramCreate,
        user_id: str
    ) -> ProgramBase:

        new_program = Program(
            title=program_data.title,
            description=program_data.description,
            native_language=program_data.native_language,
            language=program_data.language,
            level_of_experience=program_data.level_of_experience,
            user_id=int(user_id)
        )
        db.add(new_program)
        await db.commit()
        await db.refresh(new_program)

        return ProgramBase(
            id=new_program.id,
            user_id=new_program.user_id
        )