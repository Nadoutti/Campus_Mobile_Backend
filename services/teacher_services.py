from repositories import teacher_repo
from typing import Optional
from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# verifica se a senha é válida

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_teacher(email: str, password: str):

    teacher = await teacher_repo.get_teacher_by_email(email)


    if not teacher:
        return None
    
    if not verify_password(password, teacher["senha"]):
        return None
    
    await teacher_repo.update_last_login(teacher["id"])

    return teacher
    
async def create_access_token(data: dict, user: dict, expires_delta: Optional[ timedelta ] = None):
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, "your_secret_key", algorithm="HS256") # adicionar secrec key depois do almoco
    
    if user:
        user_id = user.get("id")

        await save_token(
            user_id=user_id, 
            token=encoded_jwt, 
            expires_at=expire,
        )

        return encoded_jwt
