from sqlalchemy.orm import Session
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
        query = select(models.Livro).where(
                models.Livro.id == id
                )
        return self.session.execute(query).scalars().first()