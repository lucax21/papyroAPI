from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from src.db.models import models
from typing import List

from src.schemas.usuario import UsuarioGeneros

class CrudGenero():
    def __init__(self, session: Session):
        self.session = session

    def listar_generos(self) -> List[models.Genero]:
        return self.session.query(models.Genero).all()
        

    def listar_generos_usuario(self) -> List[models.Genero]:
        return self.session.query(models.Usuario).options(joinedload(models.Usuario.genero)).where(models.Usuario.id == 1).one()
        

    def salvar_generos_usuario(self, generosUsuario: UsuarioGeneros):
        self.session.add(generosUsuario)
        return self.session.commit()
        # pass