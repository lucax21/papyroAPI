from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from src.crud.message import CrudMensagem
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado


router = APIRouter()
