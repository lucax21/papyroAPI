from sqlalchemy.orm import Session, joinedload, load_only

from src.db.models import models
from typing import List

class CrudAvaliacao():
    def __init__(self, session: Session):
        self.session = session

    def carregar_avaliacao(self, id: int):
        query = self.session.query(models.Avaliacao).options(joinedload(models.Avaliacao.usuario), joinedload(models.Avaliacao.avaliacao).options(joinedload(models.Livro.test2)),joinedload(models.Avaliacao.comentarios).options(joinedload(models.Likes.comentario)))\
        .where(models.Likes.fk_avaliacao==models.Avaliacao.id)
        # .where(models.Avaliacao.id == id)
        return query.first()