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
        query = select(models.Livro).where(
                models.Livro.id == id
                )
        return self.session.execute(query).scalars().first()

    def livros_serao_lidos(self, user_id: int):
        # dado = self.session.query(models.Livro).options(
        #             joinedload(models.Livro.livros_lendo)
        #         ).where(models.UsuarioLivro.fk_status == 1 and models.UsuarioLivro.fk_usuario == user_id
        #         ).all()
        dado = self.session.query(models.StatusUsuarioLivro).options(
                    joinedload(models.StatusUsuarioLivro.status_usuario_livros
                )
                ).filter(models.UsuarioLivro.fk_usuario == user_id, models.StatusUsuarioLivro.id == 3).all()
        # dado = self.session.query(models.Livro).select_from(models.Livro).join(models.Livro.).filter(models.UsuarioLivro.fk_usuario == user_id)
        return dado

    # def livros_estou_lendo(self, user_id: int):
    #     # dado = self.session.query(models.Livro).options(
    #     #             joinedload(models.Livro.livros_lendo)
    #     #         ).where(models.UsuarioLivro.fk_status == 1 and models.UsuarioLivro.fk_usuario == user_id
    #     #         ).all()
    #     dado = self.session.query(models.StatusUsuarioLivro).options(
    #                 joinedload(models.StatusUsuarioLivro.status_usuario_livros
    #             )
    #             ).filter(models.UsuarioLivro.fk_usuario == user_id, models.StatusUsuarioLivro.id == 1).all()
    #     # dado = self.session.query(models.Livro).select_from(models.Livro).join(models.Livro.).filter(models.UsuarioLivro.fk_usuario == user_id)
    #     return dado