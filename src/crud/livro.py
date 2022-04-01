from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql.functions import func
from sqlalchemy import insert
from src.db.models import models
from typing import List

from src.schemas.livro import LivroAvaliar

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
        
        query = self.session.query(models.Livro).options(joinedload(models.Livro.test2)).options(joinedload(models.Livro.avaliacoes).options(joinedload(models.Avaliacao.usuario)
        )).options(joinedload(models.Livro.genero)).join(models.Livro.test).join(models.UsuarioLivro.statuss).where(models.Livro.id == id).where(models.Livro.id == models.Avaliacao.fk_livro)

        return query.first()


    def pessoas_livro(self, id):
        query = self.session.query(models.Livro).options(joinedload(models.Livro.usuario)).where(models.Livro.id == id)

        return query.one()

    def avaliar_livro(self, id_user, ava: LivroAvaliar):
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