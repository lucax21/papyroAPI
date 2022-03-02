from sqlalchemy.orm import Session
from src.db.models import models
from typing import List

class CrudLivro():
    def __init__(self, session: Session):
        self.session = session

    def listar_livros(self) -> List[models.Livro]:
        
        return self.session.query(models.Livro).all()