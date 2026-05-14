from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session
from app import crud
from app.db.database import get_db
from app.core.security import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/login")


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    cred_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = verificar_token(token)
        email: str | None = payload.get("sub")
        if email is None:
            raise cred_exc
    except JWTError:
        raise cred_exc

    user = crud.obtener_usuario_email(db, email=email)
    if user is None:
        raise cred_exc
    return user


def require_admin(current_user=Depends(get_current_user)):
    if not current_user.es_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requiere rol admin"
        )
    return current_user