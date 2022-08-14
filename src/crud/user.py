from typing import List

from fastapi import HTTPException, status
from sqlalchemy import update, and_, bindparam, Integer
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func
from sqlalchemy.sql import text

from src.core import hash_provider
from src.db.models import models
from src.external_api.get_book import get_by_identifier
from src.schemas.user import User, UserUpdate, UserProfile
from src.utils.enum.reading_type import ReadingTypes
from src.utils.format_book_output import get_and_format_output, format_book_output


class CrudUser:

    def __init__(self, session: Session):
        self.session = session

    def new_user(self, user: User):
        try:
            db_usuario = models.User(nome=user.nome,
                                     email=user.email,
                                     apelido=user.apelido,
                                     senha=hash_provider.get_password_hash(user.senha),
                                     data_nascimento=user.data_nascimento,
                                     ativo=False)
            self.session.add(db_usuario)
            self.session.commit()
            self.session.refresh(db_usuario)
            return db_usuario
        except Exception:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def search_by_name(self, name: str, id_user: int, page: int):
        subquery_genres = self.session.query(models.UserGenre.fk_genre).where(models.UserGenre.fk_user == id_user).subquery()
        subquery_books = self.session.query(models.UserBook.fk_book).where(models.UserBook.fk_user == id_user).subquery()
        query = self.session.query(models.User.id,
                                   models.User.nickname,
                                   models.User.photo,
                                   func.count(models.UserGenre.fk_genre).label('common_genre'),
                                  ).where(and_(models.User.name.like('%' + name + '%'), models.UserGenre.fk_genre.in_(subquery_genres)))\
                                   .join(models.UserGenre, models.User.id == models.UserGenre.fk_user, isouter=True)\
                                   .group_by(models.User.id)\
                                   .offset(page * 20).limit(20).all()
        aux = []
        for x in query:
            query = self.session.query(func.count(models.UserBook.fk_book).label('commom_book'))\
                                    .where(and_(models.UserBook.fk_user == x.id, models.UserBook.fk_book.in_(subquery_books))).first()
            aux.append({
                'id': x.id,
                'nickname': x.nickname,
                'photo': x.photo,
                'common_genre': x.common_genre,
                'commom_book': query['commom_book']
            })
        return aux

    def current_user(self, email):
        return self.session.query(models.User.id) \
            .where(models.User.email == email).first()

    def get_by_email(self, email):
        return self.session.query(models.User.id, models.User.email, models.User.active, models.User.password,
                                  models.User.name, models.User.nickname, models.User.photo, models.User.description,
                                  models.User.formatted_birthday) \
            .where(models.User.email == email).first()

    def buscar_por_apelido(self, nickname):
        return self.session.query(models.User.nickname).filter(models.User.nickname == nickname).first()

    def get_sugestions(self, id, page):
        s = text('''
            WITH result AS(WITH aux AS (
                    SELECT ub2.fk_user sugestion, COUNT(ub.fk_book) quantity
                    from "user" u
                    JOIN user_book ub on ub.fk_user = u.id
                    JOIN user_book ub2 on ub.fk_book = ub2.fk_book and u.id <> ub2.fk_user
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY ub2.fk_user
                UNION ALL
                    SELECT r2.fk_user sugestion, COUNT(r.id) quantity
                    from "user" u
                    JOIN rate r on u.id = r.fk_user
                    JOIN rate r2 on r2.fk_book = r.fk_book and u.id <> r2.fk_user
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY r2.fk_user
                UNION all
                    SELECT c.fk_user sugestion, COUNT(r.id) quantity
                    from "user" u
                    JOIN rate r on u.id = r.fk_user
                    JOIN comment c on r.id = c.fk_rate and u.id <> c.fk_user
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY c.fk_user
                UNION ALL
                    SELECT c.fk_user sugestion, COUNT(r.id) quantity
                    from "user" u
                    JOIN comment c on u.id = c.fk_user
                    JOIN rate r on c.fk_rate = r.id and r.fk_user <> u.id
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY c.fk_user
                UNION ALL
                    SELECT ug2.fk_user sugestion, COUNT(ug.fk_genre) quantity
                    from "user" u
                    JOIN user_genre ug on u.id = ug.fk_user
                    JOIN user_genre ug2 on ug2.fk_genre = ug.fk_genre
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY ug2.fk_user
                UNION ALL
                    SELECT l.fk_user sugestion, COUNT(l.id) quantity
                    from "user" u
                    JOIN comment c on u.id = c.fk_user
                    JOIN "like" l on c.id = l.fk_comment
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY l.fk_user
                UNION ALL
                    SELECT l.fk_user sugestion, COUNT(l.id) quantity
                    from "user" u
                    JOIN rate r on u.id = r.fk_user
                    JOIN "like" l on r.id = l.fk_rate
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY l.fk_user
                    )
            SELECT sugestion, sum(quantity) as quantity
            FROM aux
            GROUP BY sugestion )
        SELECT "user".id, "user".nickname, "user".photo, result.quantity as interactions
        FROM result
            JOIN "user" on result.sugestion = "user".id
        WHERE "user".id <> :x
        ORDER BY result.quantity DESC
        OFFSET :y
        LIMIT 20
        ''')

        s = s.bindparams(bindparam('x', type_=Integer), bindparam('y', type_=Integer))
        result = self.session.execute(s, {'x': id, 'y': page}).fetchall()
        return {'data': result}

    def get_user(self, id) -> models.User:
        query = self.session.query(models.User).filter(models.User.id == id).first()

        return {'name': query.name,
                'nickname': query.nickname,
                'photo': query.photo,
                'description': query.description,
                'birthday': query.formatted_birthday}

    def get_by_id(self, id):
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
            .filter(and_(models.UserBook.fk_status == ReadingTypes.READING, models.UserBook.fk_user == id)) \
            .join(models.Book, models.Book.id == models.UserBook.fk_book) \
            .group_by(models.Book.identifier, models.Book.id).limit(1).all()

        query_books_read = self.session.query(
            models.Book.id,
            models.Book.identifier,
            func.count(models.UserBook.fk_status).label('count')) \
            .filter(and_(models.UserBook.fk_status == ReadingTypes.READ, models.UserBook.fk_user == id)) \
            .join(models.Book, models.Book.id == models.UserBook.fk_book) \
            .group_by(models.Book.identifier, models.Book.id).limit(1).all()

        query_books_to_read = self.session.query(
            models.Book.id,
            models.Book.identifier,
            func.count(models.UserBook.fk_status).label('count')) \
            .filter(and_(models.UserBook.fk_status == ReadingTypes.TO_READ, models.UserBook.fk_user == id)) \
            .join(models.Book, models.Book.id == models.UserBook.fk_book) \
            .group_by(models.Book.identifier, models.Book.id).limit(1).all()

        query_books_count = self.session.query(
            func.count(models.UserBook.fk_book).label('count'), models.UserBook.fk_status) \
            .where(and_(models.UserBook.fk_user == id))\
            .group_by(models.UserBook.fk_status).all()

        
        def arrange_book(x):
            book = format_book_output(get_by_identifier(x['identifier']))
            book.update({  
                'id': x.id,        
                'count': 0
            })
            return book
        
        def books(query_book, count_book):
            if len(query_book) > 0:
                book = list(map(arrange_book, query_book))
                book[0]['count'] = count_book
                return book
            return None
       
        aux = [0,0,0]
        for o in query_books_count:
            aux[o[1]-1] = o[0]

        return {'id': id,
                'name': query.name,
                'nickname': query.nickname,
                'photo': query.photo,
                'description': query.description,
                'booksQt': aux[ReadingTypes.READ-1],
                'birthday': query.formatted_birthday,
                'followers': query.followers,
                'books_to_read': books(query_books_to_read, aux[ReadingTypes.TO_READ-1]),
                'books_read': books(query_books_read, aux[ReadingTypes.READ-1]),
                'books_reading': books(query_books_reading, aux[ReadingTypes.READING-1])
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
            return 1
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

    def atualizar_foto(self, id_user: int, dado: str):

        try:
            stmt = update(models.User).where(models.User.id == id_user).values(photo=dado.photo)
            self.session.execute(stmt)
            self.session.commit()
            return 1
        except Exception as error:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get_company(self, id_book: int):
        readers_reading = self.session.query(models.User.id.label('id'),
                                   models.User.nickname,
                                   models.User.photo,
                            )\
                            .where(and_(models.UserBook.fk_book == id_book, models.UserBook.fk_status == ReadingTypes.READING))\
                            .join(models.UserBook, models.UserBook.fk_user == models.User.id)\
                            .limit(16).all()
        readers_read = self.session.query(models.User.id.label('id'),
                                   models.User.nickname,
                                   models.User.photo,
                            )\
                            .where(and_(models.UserBook.fk_book == id_book, models.UserBook.fk_status == ReadingTypes.READ))\
                            .join(models.UserBook, models.UserBook.fk_user == models.User.id)\
                            .limit(16).all()
        readers_to_read = self.session.query(models.User.id.label('id'),
                                   models.User.nickname,
                                   models.User.photo,
                            )\
                            .where(and_(models.UserBook.fk_book == id_book, models.UserBook.fk_status == ReadingTypes.TO_READ))\
                            .join(models.UserBook, models.UserBook.fk_user == models.User.id)\
                            .limit(16).all()

        query_status = self.session.query(models.Status).all()

        def find_status(list, value):
            for x in list:
                if x.id == value:
                    return x.status
            return 'Erro ao carregar status.'

 
        return {
            'readers_reading': {
                'id': ReadingTypes.READING,
                'status': find_status(query_status, ReadingTypes.READING),
                'readers': readers_reading,
            },
            'readers_read': {
                'id': ReadingTypes.READ,
                'status': find_status(query_status, ReadingTypes.READ),
                'readers': readers_read,
            },
            'readers_to_read': {
                'id': ReadingTypes.TO_READ,
                'status': find_status(query_status, ReadingTypes.TO_READ),
                'readers': readers_to_read,
            }
        }

    def get_company_status(self, id_book: int, id_status: int):
            query = self.session.query(models.User.id.label('id'),
                                   models.User.nickname,
                                   models.User.photo,
                            )\
                            .where(and_(models.UserBook.fk_book == id_book, models.UserBook.fk_status == id_status))\
                            .join(models.UserBook, models.UserBook.fk_user == models.User.id)\
                            .all()
            query_status = self.session.query(models.Status).where(models.Status.id == id_status).first()

            return {
            
                'id': id_status,
                'status': query_status.status if query_status.status else 'Erro, status inexistente.',
                'readers': query
            
        }
