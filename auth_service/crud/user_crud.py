from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth_service.db.models.user import User

from auth_service.schemas.user import UserCreate
from auth_service.schemas.token import AuthSchema, Token

from auth_service.services.security import pass_settings
from auth_service.services.jwt import create_access_token

from fastapi import HTTPException
from fastapi import status

class UserCrud:
    @staticmethod
    async def check_user_exists(
        db: AsyncSession,
        user_id: int
    ) -> User | None:
        query = await db.execute(
            select(User).where(User.id == user_id)
        )
        result = query.scalar_one_or_none()
        return result

    @staticmethod
    async def create_user(
        db: AsyncSession,
        user_data: UserCreate
    ) -> AuthSchema:
        is_exists = await UserCrud.check_user_exists(
            db=db, user_id=user_data.id
        )

        if is_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="user already registered"
            )
        
        hashed_password = pass_settings.get_password_hash(password=user_data.password)

        new_user = User(
            name=user_data.name,
            email=user_data.email,
            phone=user_data.phone,
            verified=False,
            password=hashed_password
        )

        db.add(new_user)
        await db.refresh()
        await db.commit()

        token = create_access_token(
            data={"sub": user_data.id}
        )

        return {
            "token": {
                "access_token": token,
                "token_type": "bearer"
            },
            "user": {
                "id": user_data.id
            }
        }
