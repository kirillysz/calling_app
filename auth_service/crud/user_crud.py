from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth_service.db.models.user import User
from auth_service.schemas.token import Token

from auth_service.schemas.user import UserCreate, UserBase
from auth_service.schemas.user_auth import UserAuth
from auth_service.schemas.token import AuthSchema

from auth_service.services.security import pass_settings
from auth_service.services.jwt import create_access_token

from fastapi import HTTPException
from fastapi import status

class UserCrud:
    @staticmethod
    async def check_user_exists(
        db: AsyncSession,
        email: str
    ) -> User | None:
        query = await db.execute(
            select(User).where(User.email == email)
        )
        result = query.scalar_one_or_none()
        return result

    @staticmethod
    async def create_user(
        db: AsyncSession,
        user_data: UserCreate
    ) -> AuthSchema:
        is_exists = await UserCrud.check_user_exists(
            db=db, email=user_data.email
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
            hashed_password=hashed_password,
            native_language=user_data.native_language,
            preferred_language=user_data.preferred_language,
            level_of_experience=user_data.level_of_experience
        )

        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        token = create_access_token(
            data={"sub": str(new_user.id)}
        )

        return AuthSchema(
            access_token=token,
            token_type="bearer",
            user=UserBase(
                id=new_user.id
            )
        )

    @staticmethod
    async def login_user(
        db: AsyncSession,
        email: str,
        password: str
    ) -> Token:
        user = await UserCrud.check_user_exists(
            db=db, email=email
        )

        if not user or not pass_settings.verify_password(plain_password=password, hashed_password=user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password"
            )
        
        token = create_access_token(
            data={"sub": str(user.id)}
        )
        return Token(access_token=token, token_type="bearer")
