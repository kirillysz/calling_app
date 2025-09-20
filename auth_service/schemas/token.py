from pydantic import BaseModel, Field

from auth_service.schemas.user import UserBase

class Token(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(..., examples=["bearer"])

class AuthSchema(BaseModel):
    token: Token
    user: UserBase