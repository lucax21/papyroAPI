from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.db.models import models
from src.schemas.genre import GenreUserNew


class CrudGenre:
    def __init__(self, session: Session):
        self.session = session

    def list_genres(self):
        return self.session.query(models.Genre).order_by(models.Genre.name).all()

    def list_user_genres(self, user_id):
        query_genres = self.session.query(models.Genre.id, models.Genre.name, models.Genre.description) \
            .order_by(models.Genre.name).all()

        query_genres_select = self.session.query(models.Genre.id, models.UserGenre.fk_user) \
            .where(models.UserGenre.fk_user == user_id) \
            .join(models.UserGenre, models.Genre.id == models.UserGenre.fk_genre) \
            .all()

        aux = [False] * len(query_genres)
        for x in query_genres_select:
            aux[x['id'] - 1] = True

        result = []
        for x in query_genres:
            result.append({
                'id': x.id,
                'name': x.name,
                'description': x.description,
                'select_genre': aux[x.id - 1]
            })

        return result

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
