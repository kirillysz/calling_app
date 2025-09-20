from pydantic import BaseModel, Field

class UserBase(BaseModel):
    id: int = Field(..., examples=[1])

class UserCreate(BaseModel):
    name: str = Field(..., examples=["Kirill"])
    email: str = Field(..., examples=["kirisa49@gmail.com"])

    phone: str = Field(..., examples=["+7 777 888 23 02"])
    verified: bool = Field(default=False, examples=[False])
    
    password: str = Field(..., examples=["YourPassword"])

    native_language: str = Field(default=None, examples=["Russian"])
    preferred_language: str = Field(default=None, examples=["English"])
    level_of_experience: int = Field(default=None, examples=[3])
