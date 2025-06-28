from fastapi import APIRouter, HTTPException, status, Depends
from models.token_models import Token
from fastapi.security import OAuth2PasswordRequestForm
from services import teacher_services
from datetime import datetime, timedelta

router = APIRouter(prefix="/teacher", tags=["Teacher"])


# rota de login

@router.post("/login", response_model=Token)
async def login_teacher(form_data: OAuth2PasswordRequestForm = Depends()):
    
    # autenticando usuario verifiando seu nome e senha
    user = await teacher_services.authenticate_teacher(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # gerando o token de acesso
    access_token_expires = timedelta(minutes=30)
    access_token = await teacher_services.create_access_token(
        data={"sub": user["id"], "role": "teacher"},
        user=user,
        expires_delta=access_token_expires
    )
