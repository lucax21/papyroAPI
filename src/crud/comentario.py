from sqlalchemy import insert
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import Session, joinedload, lazyload

from fastapi import HTTPException, status

from src.schemas.comentario import ComentarioSalvar
from src.db.models import models
from typing import List

class CrudComentario():
    def __init__(self, session: Session):
        self.session = session

    def salvar_comentario(self, id_user: int, dado: ComentarioSalvar):
        try:
            stmt = models.Comentario(fk_livro=dado.id_livro,
                                                                fk_usuario=id_user,
                                                                data_criacao=func.now(),
                                                                texto=dado.texto,
                                                                likes=0,
                                                                nota=dado.nota
                                                                )                                     
            self.session.add(stmt)
            self.session.commit()
            self.session.refresh(stmt)
    
            stmt2 = models.Likes(fk_comentario=stmt.id, fk_avaliacao=dado.id_avaliacao, fk_usuario=stmt.fk_usuario)
            self.session.add(stmt2)
            self.session.commit()
            self.session.refresh(stmt2)
            return stmt2
        except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)