from typing import List

from fastapi import HTTPException, status
from sqlalchemy import select, update, insert, and_
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql.functions import func

from src.core import hash_provider
from src.db.models import models
from src.external_api.get_book import get_by_identifier
from src.schemas.usuario import Usuario, UsuarioAddLivroBiblioteca, UserUpdate, UsuarioPerfil
from src.utils.format_book_output import get_and_format_output


# Apagar
def get_book_simple_infos(data):
    if data:
        book = get_by_identifier(data.identifier)

        if "volumeInfo" not in book:
            raise HTTPException(status_code=404, detail='Não encontrado')

        if isinstance(book, str):
            raise HTTPException(status_code=400, detail=book)

        return {'id': data.id,
                'book_title': book['volumeInfo']['title'],
                'cover': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book[
                    'volumeInfo'] else 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1591030940l/50998096.jpg',
                'author': book['volumeInfo']['authors']}
    return {}


def get_list_book_simple_infos(data):
    books = []
    for item in data:
        if data:
            book = get_by_identifier(item.identifier)

            if "volumeInfo" not in book:
                raise HTTPException(status_code=404, detail='Não encontrado')

            if isinstance(book, str):
                raise HTTPException(status_code=400, detail=book)

            books.append({'id': item.id,
                          'book_title': book['volumeInfo']['title'],
                          'cover': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book[
                              'volumeInfo'] else 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1591030940l/50998096.jpg',
                          'author': book['volumeInfo']['authors']})

    return books


#######################33


class CrudUsuario:

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
        except Exception:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # função para testes
    def listar(self) -> List[models.User]:
        aa = self.session.execute(select(models.User))
        return aa.scalars().all()

    def buscar_por_nome(self, nome) -> List[models.User]:

        return self.session.query(models.User).filter(models.User.nome.like(nome + '%')).all()

    def buscar_por_email(self, email) -> models.User:
        query = select(models.User).where(
            models.User.email == email
        )
        return self.session.execute(query).scalars().first()

    def buscar_por_apelido(self, nickname):
        return self.session.query(models.User.nickname).filter(models.User.nickname == nickname).first()

    def get_user(self, id) -> models.User:
        query = self.session.query(models.User).filter(models.User.id == id).first()

        return {'name': query.name,
                'nickname': query.nickname,
                'photo': query.photo,
                'description': query.description,
                'birthday': query.formatted_birthday, }

    def get_by_id(self, id) -> models.User:
        query = self.session.query(models.User.id,
                                   models.User.name,
                                   func.count(models.Friend.fk_destiny).label('followers'),
                                   models.User.formatted_birthday,
                                   models.User.nickname,
                                   models.User.photo,
                                   models.User.description) \
            .join(models.Friend, models.Friend.fk_destiny == id, isouter=True) \
            .filter(models.User.id == id) \
            .group_by(models.User).first()

        if not query:
            raise HTTPException(status_code=404, detail='Não encontrado')

        query_books_reading = self.session.query(
            models.Book.id,
            models.Book.identifier,
            func.count(models.UserBook.fk_status).label('count')) \
            .filter(and_(models.UserBook.fk_status == 1, models.UserBook.fk_user == id)) \
            .join(models.Book, models.Book.id == models.UserBook.fk_book, isouter=True) \
            .group_by(models.Book.identifier, models.Book.id).limit(1).all()

        query_books_read = self.session.query(
            models.Book.id,
            models.Book.identifier,
            func.count(models.UserBook.fk_status).label('count')) \
            .filter(and_(models.UserBook.fk_status == 2, models.UserBook.fk_user == id)) \
            .join(models.Book, models.Book.id == models.UserBook.fk_book, isouter=True) \
            .group_by(models.Book.identifier, models.Book.id).limit(1).all()

        query_books_to_read = self.session.query(
            models.Book.id,
            models.Book.identifier,
            func.count(models.UserBook.fk_status).label('count')) \
            .filter(and_(models.UserBook.fk_status == 3, models.UserBook.fk_user == id)) \
            .join(models.Book, models.Book.id == models.UserBook.fk_book, isouter=True) \
            .group_by(models.Book.identifier, models.Book.id).limit(1).all()

        query_books_reading_count = self.session.query(
            func.count(models.UserBook.fk_book).label('count')) \
            .filter(and_(models.UserBook.fk_user == id, models.UserBook.fk_status == 1)) \
            .one()

        query_books_read_count = self.session.query(
            func.count(models.UserBook.fk_book).label('count')) \
            .filter(and_(models.UserBook.fk_user == id, models.UserBook.fk_status == 2)) \
            .one()

        query_books_to_read_count = self.session.query(
            func.count(models.UserBook.fk_book).label('count')) \
            .filter(and_(models.UserBook.fk_user == id, models.UserBook.fk_status == 3)) \
            .one()

        formated_books_reading = get_list_book_simple_infos(query_books_reading)
        formated_books_read = get_list_book_simple_infos(query_books_read)
        formated_books_to_read = get_list_book_simple_infos(query_books_to_read)

        formated_books_reading[0].update({'count': query_books_reading_count.count})

        if formated_books_read:
            formated_books_read[0]['count'] = query_books_read_count.count
        if formated_books_to_read:
            formated_books_to_read[0]['count'] = query_books_to_read_count.count

        return {'id': id,
                'name': query.name,
                'nickname': query.nickname,
                'photo': query.photo,
                'description': query.description,
                'booksQt': query_books_read_count.count,
                'birthday': query.formatted_birthday,
                'followers': query.followers,
                'books_reading': formated_books_reading,
                'books_read': formated_books_read,
                'books_to_read': formated_books_to_read
                }

    def ativar_conta(self, instancia_usu):
        try:
            update_stmt = update(models.User).where(
                models.User.id == instancia_usu.id).values(ativo=instancia_usu.ativo, confirmacao=instancia_usu.confirmacao)
            self.session.execute(update_stmt)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def atualizar_usuario(self, user_id: int, usuario: UserUpdate):

        try:
            atualizar_stmt = update(models.User).where(models.User.id == user_id).values(name=usuario.name,
                                                                                         nickname=usuario.nickname,
                                                                                         description=usuario.description,
                                                                                         birthday=usuario.birthday
                                                                                         )
            self.session.execute(atualizar_stmt)
            self.session.commit()
            # self.session.refresh(usuario)
            # return usuario
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

    def feed(self, id: int, page: int):

                            # .join(models.Rate, models.User.id == models.Rate.fk_user,  isouter=True)\
                            # .join(models.Comment, models.User.id == models.Comment.fk_user,  isouter=True)\

                                                        # .join(models.Rate, models.Rate.id == models.Comment.fk_rate, full=True)\

        # query = self.session.query(func.count(models.Comment.fk_rate).label('count_comments'),
        #                            models.Comment.id.label('id_comment'),
        #                            models.Rate.id.label('id_rate'),
        #                            models.Rate.text.label('rate'),
        #                            models.Rate.date.label('date_rate'),
        #                            models.Rate.likes.label('likes_rate'),
        #                            models.User.id.label('id_user'),
        #                            models.User.nickname.label('nickname'),
        #                            models.User.photo.label('photo'),
        #                            models.Book.id.label('id_book'),
        #                            models.Book.identifier.label('identifier')
        #                            )\
        #                     .where(models.Rate.fk_user == models.Friend.fk_destiny)\
        #                     .join(models.User, models.User.id == models.Comment.fk_user)\
        #                     .join(models.Friend, and_(models.Friend.fk_origin == id,
        #                                               models.Friend.ignored == False,
        #                                               models.Friend.pending == False))\
        #                     .join(models.Rate, models.Rate.id == models.Comment.fk_rate)\
        #                     .join(models.Book, models.Book.id == models.Rate.fk_book)\
        #                     .group_by(
        #                             models.Comment.id.label('id_comment'),
        #                             models.Rate.id.label('id_rate'),
        #                             models.Rate.text.label('text_rate'),
        #                             models.Rate.date.label('date_rate'),
        #                             models.Rate.rate.label('rate'),
        #                             models.Rate.likes.label('likes_rate'),
        #                             models.User.id.label('id_user'),
        #                             models.User.nickname,
        #                             models.User.photo,
        #                             models.Book.id.label('id_book'),
        #                             models.Book.identifier
        #                            )\
        #                     .order_by(models.Rate.date.desc())\
        #                     .offset(page * 2000).limit(2000).all()

        # query = self.session.query(func.count(models.Comment.id).label('count_comments'),
        #                            models.Comment.id.label('id_comment'),
        #                            models.Comment.text.label('comment'),
        #                            models.Rate.id.label('id_rate'),
        #                            models.Rate.text.label('rate'),
        #                            models.Rate.date.label('date_rate'),
        #                            models.Rate.likes.label('likes_rate'),
        #                            models.User.id.label('id_user'),
        #                            models.User.nickname.label('nickname'),
        #                            models.User.photo.label('photo'),
        #                            models.Like.id.label('like_id'),
        #                            models.Book.id.label('id_book'),
        #                            models.Book.identifier.label('identifier')
        #                            )\
        #                     .where(models.Rate.fk_user == models.Friend.fk_destiny)\
        #                     .join(models.User, models.User.id == models.Comment.fk_user, isouter=True)\
        #                     .join(models.Friend, and_(models.Friend.fk_origin == id,
        #                                               models.Friend.ignored == False,
        #                                               models.Friend.pending == False))\
        #                     .join(models.Rate, models.Rate.id == models.Comment.fk_rate)\
        #                     .join(models.Like, and_(models.Like.fk_rate == models.Rate.id,
        #                                 models.Like.fk_user == id,
        #                                 id is not None), isouter=True)\
        #                     .join(models.Book, models.Book.id == models.Rate.fk_book)\
        #                     .group_by(
        #                            models.Comment.id.label('id_comment'),
        #                            models.Comment.text.label('comment'),
        #                            models.Rate.id.label('id_rate'),
        #                            models.Rate.text.label('rate'),
        #                            models.Rate.date.label('date_rate'),
        #                            models.Rate.likes.label('likes_rate'),
        #                            models.User.id.label('id_user'),
        #                            models.User.nickname.label('nickname'),
        #                            models.User.photo.label('photo'),
        #                            models.Like.id.label('like_id'),
        #                            models.Book.id.label('id_book'),
        #                            models.Book.identifier.label('identifier')
        #                            )\
        #                     .order_by(models.Rate.date.desc())\
        #                     .offset(page * 20).limit(20).all()
        query = self.session.query(
                                   func.count(models.Comment.id).label('count_comments'),
                                   models.Rate.id.label('id_rate'),
                                   models.Rate.text.label('rate'),
                                   models.Rate.date.label('date_rate'),
                                   models.Rate.likes.label('likes_rate'),
                                   models.User.id.label('id_user'),
                                   models.User.nickname.label('nickname'),
                                   models.User.photo.label('photo'),
                                   models.Like.id.label('like_id'),
                                   models.Book.id.label('id_book'),
                                   models.Book.identifier.label('identifier')
                                   )\
                            .where(models.Rate.fk_user == models.Friend.fk_destiny)\
                            .join(models.User, models.User.id == models.Comment.fk_user, isouter=True)\
                            .join(models.Friend, and_(models.Friend.fk_origin == id,
                                                      models.Friend.ignored == False,
                                                      models.Friend.pending == False))\
                            .join(models.Rate, models.Rate.id == models.Comment.fk_rate, isouter=True)\
                            .join(models.Like, and_(models.Like.fk_rate == models.Rate.id,
                                        models.Like.fk_user == id,
                                        id is not None), isouter=True)\
                            .join(models.Book, models.Book.id == models.Rate.fk_book)\
                            .group_by(
                                   models.Rate.id.label('id_rate'),
                                   models.User.id.label('id_user'),
                                   models.Like.id.label('like_id'),
                                   models.Book.id.label('id_book')
                                   )\
                            .order_by(models.Rate.date.desc())\
                            .offset(page * 20).limit(20).all()

        aux = []
        for x in query:
                aa = self.session.query(func.count(models.Comment.id).label('count_comments'))\
                                    .where(models.Comment.fk_rate == x.id_rate).all()
                # aaaa = self.session.query(func.count(models.Like.id).label('count_likes'))\
                #                     .where(models.Like.fk_rate == x.id_rate).all()

                book = get_and_format_output(x['identifier'])
                book.update({'id': x['id_book']})
                aux.append({
                    'count_comments': aa[0]['count_comments'],
                    # 'count_likes': aaaa[0]['count_likes'],
                    'text': x.rate,
                    # 'date': x.date_rate,
                    'rate': x.rate,
                    'likes': x.likes_rate,
                    'user': {
                        'nickname': x.nickname,
                        'photo': x.photo,
                        'id': x.id_user
                    },
                    'book': book
                })
            
        return aux

    def user_books(self, user_id: int, reading_type: int, page: int):
        data = self.session.query(models.Book.id, models.Book.identifier,
                                  func.count(models.Rate.id).label('count'),
                                  func.sum(models.Rate.rate).label('sum')) \
            .join(models.UserBook, and_(models.UserBook.fk_book == models.Book.id,
                                        models.UserBook.fk_user == user_id,
                                        models.UserBook.fk_status == reading_type)) \
            .join(models.Rate, models.Book.id == models.Rate.fk_book, isouter=True) \
            .group_by(models.Book.id, models.Book.identifier) \
            .offset(page * 20).limit(20) \
            .all()

        def arrange_book(x):
            book = get_and_format_output(x['identifier'])
            book.update({
                'rate': x['sum'] / x['count'] if x['count'] > 0 else None,
                'id': x['id']
            })
            return book

        if len(data) > 0:
            book = list(map(arrange_book, data))
            return book

        return None

    def add_livro_biblioteca(self, id_user: int, dado: UsuarioAddLivroBiblioteca):
        query = self.session.query(models.UserLivro).where(models.UserLivro.fk_usuario == id_user).where(
            models.UserLivro.fk_livro == dado.id_livro).first()

        # update
        if query:
            stmt = update(models.UserLivro).where(models.UserLivro.fk_usuario == id_user).where(
                models.UserLivro.fk_livro == dado.id_livro).values(fk_livro=dado.id_livro,
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
        # insert
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

    def atualizar_foto(self, id_user: int, dado: str):

        try:
            stmt = update(models.User).where(models.User.id == id_user).values(photo=dado.photo)
            self.session.execute(stmt)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
