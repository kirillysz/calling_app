from pydantic import BaseModel,Field

from pydantic.types import SecretStr

class UserAuth(BaseModel):
    email: str = Field(..., example="kirisa49@gmail.com")
    password: SecretStr = Field(..., min_length=8, example="password1232305")