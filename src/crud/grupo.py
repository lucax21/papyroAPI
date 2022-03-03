from sqlalchemy.orm import Session
from sqlalchemy import select
from src.db.models import models
from typing import List

class CrudGrupo():
    def __init__(self, session: Session):
        self.session = session

    def listar_grupos(self) -> List[models.Grupo]:       
        return self.session.query(models.Grupo).all()
    
    def buscar_por_grupo(self, termo) -> List[models.Grupo]:
        return self.session.query(models.Grupo).filter(models.Grupo.nome.like(termo+'%')).all()

    def buscar_por_id(self, id) -> models.Grupo:
        query = select(models.Grupo).where(
                models.Grupo.id == id
                )
        return self.session.execute(query).scalars().first()