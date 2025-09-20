from pydantic import BaseModel, Field

from auth_service.schemas.user import UserBase

class Token(BaseModel):
    access_token: str
    token_type: str

class AuthSchema(BaseModel):
    access_token: str
    token_type: str
    user: UserBase