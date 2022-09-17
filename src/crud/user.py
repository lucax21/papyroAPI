from datetime import datetime, timedelta

from dateutil import tz
from fastapi import HTTPException, status
from sqlalchemy import update, and_, bindparam, Integer, text
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func

from src.utils import hash_provider
from src.db.models import models
from src.external_api.get_book import get_by_identifier
from src.schemas.user import UserUpdate, NewUser
from src.utils.enum.reading_type import ReadingTypes
from src.utils.format_book_output import format_book_output


class CrudUser:

    def __init__(self, session: Session):
        self.session = session
    
    def new_user(self, user: NewUser):
        try:
            stmt = models.User(name=user.name,
                               email=user.email,
                               nickname=user.nickname,
                               password=hash_provider.get_password_hash(user.password)
                               )
            self.session.add(stmt)
            self.session.commit()
            self.session.refresh(stmt)
            return stmt
        except Exception:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def search_by_name(self, name: str, id_user: int, page: int):
        subquery_genres = self.session.query(models.UserGenre.fk_genre).where(models.UserGenre.fk_user == id_user).subquery()
        subquery_books = self.session.query(models.UserBook.fk_book).where(models.UserBook.fk_user == id_user).subquery()
        query = self.session.query(models.User.id,
                                   models.User.nickname,
                                   models.User.photo,
                                   ).where(func.lower(models.User.name).like('%' + name.lower() + '%')) \
            .offset(page * 20).limit(20).all()
        aux = []
        for x in query:
            query_commom_book = self.session.query(func.count(models.UserBook.fk_book).label('commom_book')) \
                .where(and_(models.UserBook.fk_user == x.id, models.UserBook.fk_book.in_(subquery_books))).first()
            
            query_commom_genre = self.session.query(func.count(models.UserGenre.fk_genre).label('common_genre'))\
                .where(and_(models.UserGenre.fk_user == x.id, models.UserGenre.fk_genre.in_(subquery_genres))).first()
            
            aux.append({
                'id': x.id,
                'nickname': x.nickname,
                'photo': x.photo,
                'common_genre': query_commom_genre['common_genre'],
                'commom_book': query_commom_book['commom_book']
            })
        return aux

    def current_user(self, email):
        return self.session.query(models.User.id) \
            .where(models.User.email == email).first()

    def get_verification(self, email: str):
        return self.session.query(models.User.id, models.User.active, models.User.confirmation).where(
            models.User.email == email).first()

    def get_by_email(self, email: str):
        return self.session.query(models.User.id, models.User.email, models.User.password,
                                  models.User.name, models.User.nickname, models.User.photo, models.User.description,
                                  ) \
            .where(models.User.email == email).first()

    def buscar_por_apelido(self, nickname):
        return self.session.query(models.User.nickname).filter(models.User.nickname == nickname).first()

    def get_suggestions(self, id, page):
        s = text('''
            WITH result AS(WITH aux AS (
                    SELECT ub2.fk_user suggestion, COUNT(ub.fk_book) quantity
                    from "user" u
                    JOIN user_book ub on ub.fk_user = u.id
                    JOIN user_book ub2 on ub.fk_book = ub2.fk_book and u.id <> ub2.fk_user
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY ub2.fk_user
                UNION ALL
                    SELECT r2.fk_user suggestion, COUNT(r.id) quantity
                    from "user" u
                    JOIN rate r on u.id = r.fk_user
                    JOIN rate r2 on r2.fk_book = r.fk_book and u.id <> r2.fk_user
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY r2.fk_user
                UNION all
                    SELECT c.fk_user suggestion, COUNT(r.id) quantity
                    from "user" u
                    JOIN rate r on u.id = r.fk_user
                    JOIN comment c on r.id = c.fk_rate and u.id <> c.fk_user
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY c.fk_user
                UNION ALL
                    SELECT c.fk_user suggestion, COUNT(r.id) quantity
                    from "user" u
                    JOIN comment c on u.id = c.fk_user
                    JOIN rate r on c.fk_rate = r.id and r.fk_user <> u.id
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY c.fk_user
                UNION ALL
                    SELECT ug2.fk_user suggestion, COUNT(ug.fk_genre) quantity
                    from "user" u
                    JOIN user_genre ug on u.id = ug.fk_user
                    JOIN user_genre ug2 on ug2.fk_genre = ug.fk_genre
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY ug2.fk_user
                UNION ALL
                    SELECT l.fk_user suggestion, COUNT(l.id) quantity
                    from "user" u
                    JOIN comment c on u.id = c.fk_user
                    JOIN "like" l on c.id = l.fk_comment
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY l.fk_user
                UNION ALL
                    SELECT l.fk_user suggestion, COUNT(l.id) quantity
                    from "user" u
                    JOIN rate r on u.id = r.fk_user
                    JOIN "like" l on r.id = l.fk_rate
                    WHERE 1 = 1
                    and u.id = :x
                    GROUP BY l.fk_user
                    )
            SELECT suggestion, sum(quantity) as quantity
            FROM aux
            GROUP BY suggestion )
        SELECT "user".id, "user".nickname, "user".photo, result.quantity as interactions
        FROM result
            JOIN "user" on result.suggestion = "user".id
        WHERE "user".id <> :x 
            AND "user".id NOT IN (SELECT f.fk_destiny FROM friend f where f.fk_origin = id)
        ORDER BY result.quantity DESC
        OFFSET :y
        LIMIT 20
        ''')

        s = s.bindparams(bindparam('x', type_=Integer), bindparam('y', type_=Integer))
        result = self.session.execute(s, {'x': id, 'y': page}).fetchall()
        return {'data': result}

    def get_by_id(self, id, current_user):
        query = self.session.query(models.User.id,
                                   models.User.name,
                                   func.count(models.Friend.fk_destiny).label('followers'),
                                   models.User.nickname,
                                   models.User.photo,
                                   models.User.description) \
            .join(models.Friend, models.Friend.fk_destiny == id, isouter=True) \
            .filter(models.User.id == id) \
            .group_by(models.User).first()

        if not query:
            raise HTTPException(status_code=404, detail='Não encontrado')

        you_follow = self.session.query(models.Friend).where(
            and_(models.Friend.fk_destiny == id, models.Friend.fk_origin == current_user)).first()
        query_books_count = self.session.query(
            func.count(models.UserBook.fk_book).label('count'), models.UserBook.fk_status) \
            .where(and_(models.UserBook.fk_user == id)) \
            .group_by(models.UserBook.fk_status).all()

        def arrange_book(x):
            book = format_book_output(get_by_identifier(x['identifier']))
            book.update({
                'id': x.id,
                'count': 0
            })
            return book

        aux = [0, 0, 0]
        for o in query_books_count:
            aux[o[1] - 1] = o[0]

        return {'id': id,
                'name': query.name,
                'nickname': query.nickname,
                'photo': query.photo if query.photo is not None and query.photo != '' else 'https://i.pinimg.com/736x/67/4f/c5/674fc554838de6abdbf274bdc0ca446c.jpg',
                'description': query.description,
                'booksQt': aux[ReadingTypes.READ - 1],
                'followers': query.followers,
                'you_follow': True if you_follow else False
                }

    def reset_password(self, email, pw: str):
        try:

            update_stmt = update(models.User).where(
                models.User.email == email).values(code_otp_time=None, code_otp=None,
                                                   password=hash_provider.get_password_hash(pw))

            self.session.execute(update_stmt)
            self.session.commit()
            return 1
        except Exception:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update_user(self, user_id: int, user: UserUpdate):
        try:
            stmt = update(models.User).where(models.User.id == user_id).values(name=user.name,
                                                                               nickname=user.nickname,
                                                                               description=user.description
                                                                               )
            self.session.execute(stmt)
            self.session.commit()
            return 1
        except Exception as error:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def check_reset_password_code(self, code: str, email: str):

        recent = datetime.now(tz=tz.tzlocal()) - timedelta(minutes=5)

        return self.session.query(models.User.id) \
            .where(and_(models.User.email == email, models.User.code_otp == code,
                        models.User.code_otp_time >= recent
                        )) \
            .first()

    def save_reset_code(self, email, code_otp):

        stmt = update(models.User).where(models.User.email == email).values(code_otp=code_otp, code_otp_time=func.now())
        self.session.execute(stmt)
        self.session.commit()
        return 1


    def update_photo(self, id_user: int, photo: str):

        try:
            stmt = update(models.User).where(models.User.id == id_user).values(photo=photo)
            self.session.execute(stmt)
            self.session.commit()
            return 1
        except Exception as error:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

