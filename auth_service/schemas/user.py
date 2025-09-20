from pydantic import BaseModel, Field
from pydantic.types import SecretStr

class UserBase(BaseModel):
    id: int = Field(..., examples=[1])

class UserCreate(BaseModel):
    name: str = Field(..., examples=["Kirill"])
    email: str = Field(..., examples=["kirisa49@gmail.com"])

    phone: str = Field(..., examples=["+7 777 888 23 02"])
    verified: bool = Field(default=False, examples=[False])
    
    password: SecretStr = Field(..., examples=["YourPassword"])
