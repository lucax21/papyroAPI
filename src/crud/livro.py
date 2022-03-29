from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from src.db.models import models
from typing import List

class CrudLivro():
    def __init__(self, session: Session):
        self.session = session

    def listar_livros(self) -> List[models.Livro]:
        
        return self.session.query(models.Livro).all()
    
    def buscar_por_nome(self, termo) -> List[models.Livro]:

        return self.session.query(models.Livro).filter(models.Livro.nome.like(termo+'%')).all()
    
    def buscar_por_id(self, id) -> models.Livro:
        # query = select(models.Livro).where(
        #         models.Livro.id == id
        #         )
        # return self.session.execute(query).scalars().first()
        
        query = self.session.query(models.Livro).options(joinedload(models.Livro.avaliacoes).options(joinedload(models.Avaliacao.usuario)
        # ,joinedload(models.Likes.comentario)
        )).where(models.Livro.id == id).where(models.Livro.id == models.Avaliacao.fk_livro)

        return query.all()


    def pessoas_livro(self, id):
        query = self.session.query(models.Livro).options(joinedload(models.Livro.usuario)).where(models.Livro.id == id)

        return query.one()
