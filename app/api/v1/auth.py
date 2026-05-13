from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import get_db
from app.deps import get_current_user, require_admin
from app.schemas import Token
from app.core.security import verify_password
from app.core.security import crear_token

router = APIRouter()


@router.post("", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.crear_usuario(db, usuario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.obtener_usuario_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    token = crear_token(sub=user.email, es_admin=user.es_admin)
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=schemas.UsuarioResponse)
def leer_perfil(current_user=Depends(get_current_user)):
    return current_user


@router.get("/admin/ping")
def admin_ping(_admin=Depends(require_admin)):
    return {"ok": True, "role": "admin"}