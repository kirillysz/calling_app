from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.context import CryptContext

from auth_service.schemas.token import Token
from auth_service.schemas.user import UserCreate

from auth_service.db.session import get_db

from auth_service.crud.user_crud import UserCrud

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(prefix="/auth", tags=["auth"])
user_crud = UserCrud()

@router.post("/register", response_model=Token)
async def token(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    user_with_token = await user_crud.create_user(
        db=db,
        user_data=user_data
    )

    return user_with_token

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
) -> Token:
    token = await UserCrud.login_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )
    
    return token