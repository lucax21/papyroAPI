from sqlalchemy.orm import Session, joinedload, lazyload

from src.db.models import models
from typing import List

class CrudAvaliacao():
    def __init__(self, session: Session):
        self.session = session

    def carregar_avaliacao(self, id: int):
        query = self.session.query(models.Avaliacao).options(joinedload(models.Avaliacao.comentarios)).options(joinedload(models.Avaliacao.usuario)).where(models.Avaliacao.id == id)
        
        return query.all()