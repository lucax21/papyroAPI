from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from src.models import models
from typing import Optional, List

class CrudGenero():
    def __init__(self, session: Session):
        self.session = session

    def listar_generos(self):
        generos = self.session.query(models.Genero).all()
        return generos

    def listar_generos_usuario(self):
        generos = self.session.query(models.Usuario).options(joinedload(models.Usuario.genero)).where(models.Usuario.id == 1).one()
        return generos

    def salvar_generos(self, lista: List[int]):
        pass