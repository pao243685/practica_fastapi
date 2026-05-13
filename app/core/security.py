from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

from app.core.config import settings


def crear_token(sub: str, es_admin: bool):
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    data = {"sub": sub, "exp": expire, "es_admin": es_admin}
    token = jwt.encode(data, settings.secret_key, algorithm=settings.algorithm)
    return token


def verificar_token(token: str):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None
    


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12
)

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)