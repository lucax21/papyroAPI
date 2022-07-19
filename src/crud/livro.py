from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql.functions import func
from sqlalchemy import insert
from src.db.models import models
from typing import List

from fastapi import HTTPException, status

from src.schemas.livro import LivroAvaliar

class CrudLivro():
    def __init__(self, session: Session):
        self.session = session

    def listar_livros(self) -> List[models.Book]:
        
        return self.session.query(models.Book).all()
    
    def buscar_por_nome(self, termo) -> List[models.Book]:

        return self.session.query(models.Book).filter(models.Book.nome.like(termo+'%')).all()
    
    def buscar_por_id(self, id) -> models.Book:
        
        # query = self.session.query(models.Book).options(joinedload(models.Book.test2)).options(joinedload(models.Book.genero)).options(joinedload(models.Book.avaliacoes).options(joinedload(models.Avaliacao.usuario)
        # )).join(models.Book.test).join(models.UsuarioLivro.statuss).where(models.Book.id == id).where(models.Book.id == models.Avaliacao.fk_livro)
        query = self.session.query(models.Book).options(joinedload(models.Book.test2)).options(joinedload(models.Book.genero)).options(joinedload(models.Book.avaliacoes).options(joinedload(models.Avaliacao.usuario)
        )).where(models.Book.id == id)
        
        return query.first()


    def pessoas_livro(self, id):
        query = self.session.query(models.Book).options(joinedload(models.Book.usuario)).where(models.Book.id == id)

        return query.one()

    def avaliar_livro(self, id_user, ava: LivroAvaliar):
        try:
            stmt = insert(models.Avaliacao).values(fk_livro=ava.id_livro,
                                                                fk_usuario=id_user,
                                                                nota=ava.nota,
                                                                texto=ava.texto,
                                                                likes=0,
                                                                data_criacao=func.now()
                                                                )
            self.session.execute(stmt)
            self.session.commit()
            return 1
        except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)