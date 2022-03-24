from sqlalchemy import select, update, text
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import Session, joinedload, subqueryload,lazyload
from src.schemas.usuario import Usuario, UsuarioCriar, UsuarioPerfil
from src.db.models import models
from typing import List

from src.core import hash_provider

class CrudUsuario():

    def __init__(self, session: Session):
        self.session = session

    def criar_usuario(self, usuario: Usuario):
        db_usuario = models.Usuario(nome=usuario.nome,
                email=usuario.email,
                apelido=usuario.apelido,
                senha=hash_provider.get_password_hash(usuario.senha),
                data_nascimento=usuario.data_nascimento,
                ativo=False)
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario
    
    #função para testes
    def listar(self) -> List[models.Usuario]:
        aa = self.session.execute(select(models.Usuario))
        return aa.scalars().all()
        
    def buscar_por_nome(self, nome) -> List[models.Usuario]:

        return self.session.query(models.Usuario).filter(models.Usuario.nome.like(nome+'%')).all()

    def buscar_por_email(self, email) -> models.Usuario:
        query = select(models.Usuario).where(
                models.Usuario.email == email
                )
        return self.session.execute(query).scalars().first()

    def buscar_por_apelido(self, apelido) -> models.Usuario:
        query = select(models.Usuario).where(
                models.Usuario.apelido == apelido
                )
        return self.session.execute(query).scalars().first()

    def buscar_por_id(self, id) -> models.Usuario:
        query = select(models.Usuario).where(
                models.Usuario.id == id
                )
        return self.session.execute(query).scalars().first()

    def ativar_conta(self, instancia_usu):
        update_stmt = update(models.Usuario).where(
            models.Usuario.id == instancia_usu.id).values(ativo=instancia_usu.ativo, confirmacao=instancia_usu.confirmacao)
        self.session.execute(update_stmt)
        self.session.commit()

    def atualizar_usuario(self, user_id: int, usuario: UsuarioCriar):
        if usuario.senha and usuario.senha_confirmacao:
            atualizar_stmt = update(models.Usuario).where(models.Usuario.id == user_id).values(nome=usuario.nome,
                                                            apelido=usuario.apelido,
                                                            foto=usuario.foto,
                                                            email=usuario.email,
                                                            descricao=usuario.descricao
                                                            ,
                                                            senha=hash_provider.get_password_hash(usuario.senha),
                                                            data_nascimento=usuario.data_nascimento
                                                            )
        else:
            atualizar_stmt = update(models.Usuario).where(models.Usuario.id == user_id).values(nome=usuario.nome,
                                                            apelido=usuario.apelido,
                                                            foto=usuario.foto,
                                                            email=usuario.email,
                                                            descricao=usuario.descricao
                                                            )
        self.session.execute(atualizar_stmt)
        self.session.commit()
        # self.session.refresh(usuario)

    def desabilitar_confirmação(self, user_id: int):
        atualizar_stmt = update(models.Usuario).where(models.Usuario.id == user_id).values(ativo=False)
        self.session.execute(atualizar_stmt)
        self.session.commit()

    def perfil_usuario(self, user_id: int) -> UsuarioPerfil:
       
        dado = self.session.query(models.Usuario).options(
                joinedload(models.Usuario.grupos),
                joinedload(models.Usuario.livros_lidos),
                joinedload(models.Usuario.livros_lerei),
                joinedload(models.Usuario.livros_lendo)
                ).where(
                    models.Usuario.id == user_id
                ).one()
      
        return dado
    
    def livros_serao_lidos(self, user_id: int):
        query = self.session.execute(select(models.Livro,models.Autor
              ).join(models.Livro.test).join(models.UsuarioLivro.statuss).join(models.Livro.autores).where(models.StatusUsuarioLivro.id==3).where(models.UsuarioLivro.fk_usuario == user_id))
        return query.all()

    def livros_estou_lendo(self, user_id: int):
        query = self.session.execute(select(models.Livro
              ).join(models.Livro.test).join(models.UsuarioLivro.statuss).where(models.StatusUsuarioLivro.id==2).where(models.UsuarioLivro.fk_usuario == user_id))
        return query.scalars().all()

    def livros_lidos(self, user_id: int):
        query = self.session.execute(select(models.Livro
              ).join(models.Livro.test).join(models.UsuarioLivro.statuss).where(models.StatusUsuarioLivro.id==1).where(models.UsuarioLivro.fk_usuario == user_id))
        return query.scalars().all()