from jose.exceptions import JWTError

from jose import jwt
from datetime import datetime, timedelta, timezone

from auth_service.config import get_auth_data, settings

from fastapi.security import OAuth2PasswordBearer, HTTPBearer

security = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
auth_data = get_auth_data()

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})

    auth_data = get_auth_data()

    encode_jwt = jwt.encode(
        to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    
    return encode_jwt


def decrypt_token(token: str) -> dict | bool:
    try:
        return jwt.decode(token=token, key=auth_data["secret_key"])
    except JWTError as _err:
        return False
