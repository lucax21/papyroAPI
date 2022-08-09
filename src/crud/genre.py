from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload

from src.db.models import models
from src.schemas.genre import GenreUserNew
from src.schemas.user import UserGenre


class CrudGenre:
    def __init__(self, session: Session):
        self.session = session

    def list_genres(self) -> List[models.Genre]:
        return self.session.query(models.Genre).all()

    def list_user_genres(self, user_id) -> UserGenre:

        dado = self.session.query(models.User).options(joinedload(models.User.generos)).where(
            models.User.id == user_id).one()
        # return UsuarioGeneros.from_orm(dado)
        return dado

    def save_user_genres(self, userGenre: List[GenreUserNew], user_id):
        try:
            for i in userGenre:
                id_genero = i.idGenero
                print(id_genero)
                self.session.execute(models.user_genre.insert().values(fk_usuario=user_id, fk_genero=id_genero))
                self.session.commit()
            return userGenre
        except Exception as error:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
