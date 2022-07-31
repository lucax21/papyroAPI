from sqlalchemy import insert
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import Session, joinedload, lazyload, aliased
from sqlalchemy import and_

from fastapi import HTTPException, status

# from src.schemas.comment import SaveComment
from src.db.models.models import *
from typing import List


class CrudComment:
    def __init__(self, session: Session):
        self.session = session

    # def salvar_comentario(self, id_user: int, dado: SaveComment):
    #     try:
    #         stmt = models.Comentario(fk_livro=dado.id_livro, fk_usuario=id_user, data_criacao=func.now(), texto=dado.texto,
    #                                  likes=0, nota=dado.nota)
    #         self.session.add(stmt)
    #         self.session.commit()
    #         self.session.refresh(stmt)
    #
    #         stmt2 = models.Likes(fk_comentario=stmt.id, fk_avaliacao=dado.id_avaliacao, fk_usuario=stmt.fk_usuario)
    #         self.session.add(stmt2)
    #         self.session.commit()
    #         self.session.refresh(stmt2)
    #         return stmt2
    #     except Exception as error:
    #         self.session.rollback()
    #         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_comments(self, rate_id, user_id):
        review = self.session.query(Rate, Book, Like.id, User.id, User.photo, User.nickname)\
            .where(Rate.id == rate_id) \
            .join(Book, Rate.fk_book == Book.id) \
            .join(User, User.id == Rate.fk_user) \
            .join(Like, and_(Like.fk_user == user_id, Like.fk_rate == rate_id), isouter=True).first()

        data = self.session.query(Comment.id, Comment.text, Comment.date, Comment.likes,
                                  User.id, User.nickname, User.photo,
                                  Like.id) \
            .where(Comment.fk_rate == rate_id) \
            .join(User, User.id == Comment.fk_user) \
            .join(Like, Like.fk_user == user_id, isouter=True).all()

        # def format_comment(comment):
        #     return {
        #         'user': {
        #             'id': comment['id']
        #         }
        #     }
        return data