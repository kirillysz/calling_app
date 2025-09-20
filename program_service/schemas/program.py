from pydantic import BaseModel, Field

class ProgramBase(BaseModel):
    id: int = Field(..., examples=[1])
    user_id: int = Field(..., examples=[1])

class ProgramCreate(BaseModel):
    title: str = Field(..., examples=["English"])
    description: str = Field(..., examples=["Learn English A1"])
    language: str = Field(..., examples=["English"])
    
    native_language: str = Field(..., examples=["Russian"])
    language: str = Field(..., examples=["English"])
    level_of_experience: int = Field(..., examples=[1])
