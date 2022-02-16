from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas.genero import Genero
from src.models import models

class CrudGenero():
    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        generos = self.session.query(models.Genero).all()
        return generos
