from sqlalchemy import select, update, insert
from sqlalchemy.sql.functions import func
from sqlalchemy.orm import Session, joinedload, subqueryload,lazyload
from src.schemas.usuario import AtualizarFoto, Usuario, UsuarioAddLivroBiblioteca, UsuarioCriar, UsuarioPerfil
from src.db.models import models
from typing import List

from fastapi import HTTPException, status

from src.core import hash_provider

class CrudUsuario():

    def __init__(self, session: Session):
        self.session = session

    def criar_usuario(self, usuario: Usuario):
        try:
            db_usuario = models.User(nome=usuario.nome,
                    email=usuario.email,
                    apelido=usuario.apelido,
                    senha=hash_provider.get_password_hash(usuario.senha),
                    data_nascimento=usuario.data_nascimento,
                    ativo=False)
            self.session.add(db_usuario)
            self.session.commit()
            self.session.refresh(db_usuario)
            return db_usuario
        except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #função para testes
    def listar(self) -> List[models.User]:
        aa = self.session.execute(select(models.User))
        return aa.scalars().all()
        
    def buscar_por_nome(self, nome) -> List[models.User]:

        return self.session.query(models.User).filter(models.User.nome.like(nome+'%')).all()

    def buscar_por_email(self, email) -> models.User:
        query = select(models.User).where(
                models.User.email == email
                )
        return self.session.execute(query).scalars().first()

    def buscar_por_apelido(self, apelido) -> models.User:
        query = select(models.User).where(
                models.User.apelido == apelido
                )
        return self.session.execute(query).scalars().first()

    def buscar_por_id(self, id) -> models.User:
        query = select(models.User).where(
                models.User.id == id
                )
        return self.session.execute(query).scalars().first()

    def ativar_conta(self, instancia_usu):
        try:
            update_stmt = update(models.User).where(
                models.User.id == instancia_usu.id).values(ativo=instancia_usu.ativo, confirmacao=instancia_usu.confirmacao)
            self.session.execute(update_stmt)
            self.session.commit()
        except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def atualizar_usuario(self, user_id: int, usuario: UsuarioCriar):
  

        try:
            atualizar_stmt = update(models.User).where(models.User.id == user_id).values(nome=usuario.nome,
                                                                apelido=usuario.apelido,
                                                                descricao=usuario.descricao,
                                                                data_nascimento=usuario.data_nascimento
                                                                )
            self.session.execute(atualizar_stmt)
            self.session.commit()
        # self.session.refresh(usuario)
        except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def desabilitar_confirmação(self, user_id: int):
        try:
            atualizar_stmt = update(models.User).where(models.User.id == user_id).values(ativo=False)
            self.session.execute(atualizar_stmt)
            self.session.commit()
        except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perfil_usuario(self, user_id: int) -> UsuarioPerfil:
       
        dado = self.session.query(models.User).options(
                joinedload(models.User.grupos),
                joinedload(models.User.livros_lidos).options(joinedload(models.Book.test2)),
                joinedload(models.User.livros_lerei).options(joinedload(models.Book.test2)),
                joinedload(models.User.livros_lendo).options(joinedload(models.Book.test2))
                ).where(
                    models.User.id == user_id
                ).one()

        return dado
    
    def livros_serao_lidos(self, user_id: int):
        query = self.session.query(models.Book).options(
            joinedload(models.Book.test2)).join(models.Book.test).join(models.UserLivro.statuss).where(models.StatusUsuarioLivro.id==3).where(models.UserLivro.fk_usuario == user_id)
        return query.all()

    def livros_lendo(self, user_id: int):
        query = self.session.query(models.Book).options(
            joinedload(models.Book.test2)).join(models.Book.test).join(models.UserLivro.statuss).where(models.StatusUsuarioLivro.id==2).where(models.UserLivro.fk_usuario == user_id)
        return query.all()

    def livros_lidos(self, user_id: int) -> models.Book:
        query = self.session.query(models.Book).options(
            joinedload(models.Book.test2)).join(models.Book.test).join(models.UserLivro.statuss).where(models.StatusUsuarioLivro.id==1).where(models.UserLivro.fk_usuario == user_id)
        
        # testar iss-> p = db.query(Profile).options(joinedload('*')).filter_by(id=p.id).limit(1).one()'
        return query.all()

    def add_livro_biblioteca(self, id_user: int, dado: UsuarioAddLivroBiblioteca):
        query = self.session.query(models.UserLivro).where(models.UserLivro.fk_usuario==id_user).where(models.UserLivro.fk_livro == dado.id_livro).first()
        
        # update
        if query:
            stmt = update(models.UserLivro).where(models.UserLivro.fk_usuario == id_user).where(models.UserLivro.fk_livro == dado.id_livro).values(fk_livro=dado.id_livro,
                                                            fk_usuario=id_user,
                                                            fk_status=dado.id_status,
                                                            data_entrada=func.now()
                                                            )
            try:
                self.session.execute(stmt)
                self.session.commit()
            except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #insert
        else:
            # self.session.execute(models.UserLivro.insert().values(fk_usuario=id_user,fk_livro=dado.id_livro, fk_status=dado.id_status))
            stmt = insert(models.UserLivro).values(fk_livro=dado.id_livro,
                                                            fk_usuario=id_user,
                                                            fk_status=dado.id_status,
                                                            data_entrada=func.now()
                                                            )
            try:
                self.session.execute(stmt)
                self.session.commit()
            except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def atualizar_foto(self, id_user: int, dado: AtualizarFoto):

        try:
            stmt = update(models.User).where(models.User.id == id_user).values(foto=dado.link)
            self.session.execute(stmt)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)