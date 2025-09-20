from fastapi import APIRouter, Depends, HTTPException, Request

from starlette.status import HTTP_201_CREATED

from sqlalchemy.ext.asyncio import AsyncSession
from auth_service.services.jwt import decrypt_token

from program_service.db.session import get_db
from program_service.crud.program_crud import ProgramCrud

from program_service.schemas.program import ProgramCreate, ProgramBase

router = APIRouter(prefix="/programs", tags=["programs"])

@router.post("/", response_model=ProgramBase, status_code=HTTP_201_CREATED)
async def create_program(
    program_data: ProgramCreate,
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    headers = request.headers

    if "Authorization" not in headers:
        raise HTTPException(status_code=401, detail="Authentication required")

    token = headers.get("Authorization").split(" ")[1]
    user_id = decrypt_token(token=token)
    print(user_id)

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    response = await ProgramCrud.create_program(
        db=db, program_data=program_data, user_id=user_id
    )
    return response
