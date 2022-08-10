from sqlalchemy.orm import Session, joinedload

from src.db.models import models


class CrudAvaliacao():
    def __init__(self, session: Session):
        self.session = session

    def carregar_avaliacao(self, id: int):
        query = self.session.query(models.Rate).options(joinedload(models.Rate.usuario),
                                                        joinedload(models.Rate.avaliacao).options(
                                                            joinedload(models.Book.test2)),
                                                        joinedload(models.Rate.comentarios).options(
                                                            joinedload(models.Like.comentario))) \
            .where(models.Like.fk_avaliacao == models.Rate.id)
        # .where(models.Avaliacao.id == id)
        return query.first()
