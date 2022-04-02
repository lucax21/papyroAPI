from sqlalchemy.orm import Session, joinedload

from src.db.models import models
from typing import List

class CrudAmigo():
    def __init__(self, session: Session):
        self.session = session

    def carregar_conversas(self, id: int):
        query = self.session.query(models.Usuario.amigos_origem)
        #.options(joinedload(models.Amigo.usuario_origem)).where(models.Amigo.fk_origem==1)
        return query.all()