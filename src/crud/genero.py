from sqlalchemy import select, update
from sqlalchemy.orm import Session, joinedload

from src.db.models import models
from typing import List

from fastapi import HTTPException, status

from src.schemas.genero import GeneroUsuarioCriar

class CrudGenero():
    def __init__(self, session: Session):
        self.session = session

    def get_genres_user(self, id_user: int):
        query_genres = self.session.query(models.Genre.id, models.Genre.name, models.Genre.description)\
                                    .order_by(models.Genre.name).all()

     
        query_genres_select = self.session.query(models.Genre.id, models.UserGenre.fk_user)\
                            .where(models.UserGenre.fk_user == id_user)\
                            .join(models.UserGenre, models.Genre.id == models.UserGenre.fk_genre)\
                            .all()

        aux = [False]*len(query_genres)
        for x in query_genres_select:
            aux[x['id']-1]=True

        result=[]
        for x in query_genres:
            result.append({
                'id': x.id,
                'name': x.name,
                'description': x.description,
                'select_genre': aux[x.id-1]
            })

        return result

    def get_genres(self):
        return self.session.query(models.Genre.id, models.Genre.name, models.Genre.description)\
                                    .order_by(models.Genre.name).all()

    def salvar_generos_usuario(self, generosUsuario: List[GeneroUsuarioCriar], user_id):
 
        try:
            for i in generosUsuario:
                id_genero = i.idGenero
                print(id_genero)
                self.session.execute(models.usuario_genero.insert().values(fk_usuario=user_id,fk_genero=id_genero))
                self.session.commit()
            return generosUsuario
        except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
