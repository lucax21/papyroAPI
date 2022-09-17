from typing import List

from fastapi import HTTPException, status
from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.db.models import models
from src.schemas.genre import GenreUserNew


class CrudGenre:
    def __init__(self, session: Session):
        self.session = session

    def get_list_user_genres(self, user_id):
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

    def save_user_genres(self, id_user: int, id_genre: int, mode: bool):
        genre_obj = self.session.query(models.UserGenre).where(and_(models.UserGenre.fk_user == id_user, models.UserGenre.fk_genre == id_genre)).first()
        if mode and not genre_obj:        
            stmt = models.UserGenre(fk_user=id_user, fk_genre=id_genre)
            self.session.add(stmt)
            self.session.commit()
            return 1
        if not mode and genre_obj:
            self.session.delete(genre_obj)
            self.session.commit()
            return -1

