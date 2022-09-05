from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func
from src.db.models import models
from src.utils.format_book_output import get_and_format_output

from sqlalchemy.sql.expression import literal

class CrudFeed:

    def __init__(self, session: Session):
        self.session = session

    def feed(self, id: int, page: int):

        rates = self.session.query(
                                   models.Rate.date.label('date'),
                                   models.Rate.formatted_date,
                                   models.User.id.label('id_user'),
                                   models.User.nickname.label('nickname'),
                                   models.User.photo.label('photo'),
                                   models.Rate.id.label('id_rate'),
                                   models.Rate.text,
                                   models.Rate.rate.label('rate'),
                                   models.Rate.likes,
                                   models.Rate.rate,
                                   models.Book.id.label('id_book'),
                                   models.Book.identifier.label('identifier'),
                                   models.Like.id.label('like_id'),
                                   literal('r').label("type")
                                   )\
                    .where(and_(
                                models.Friend.fk_origin==id
                                ))\
                    .join(models.Friend, models.User.id == models.Friend.fk_destiny)\
                    .join(models.Rate, models.User.id == models.Rate.fk_user)\
                    .join(models.Like, and_(models.Like.fk_rate == models.Rate.id,
                                        models.Like.fk_user == id,
                                        id is not None), isouter=True)\
                    .join(models.Book, models.Book.id == models.Rate.fk_book)\
                    .order_by(models.Rate.date.desc())\
                    .offset(page * 8).limit(8).all()
      
        comments = self.session.query(
                                    models.Comment.date.label('date'),
                                    models.Comment.formatted_date,
                                    models.User.id.label('id_user'),
                                    models.User.nickname.label('nickname'),
                                    models.User.photo.label('photo'),
                                    models.Rate.id.label('id_rate'),
                                    models.Comment.id.label('id_comment'),
                                    models.Comment.text,
                                    models.Comment.likes,
                                    models.Book.id.label('id_book'),
                                    models.Book.identifier.label('identifier'),
                                    models.Like.id.label('like_id'),
                                    literal('c').label("type")
                                    )\
                                .where(and_(
                                models.Friend.fk_origin==id
                                ))\
                            .join(models.Friend, models.User.id == models.Friend.fk_destiny)\
                            .join(models.Comment, models.Comment.fk_user == models.User.id)\
                            .join(models.Rate, models.Rate.id == models.Comment.fk_rate)\
                            .join(models.Like, and_(models.Like.fk_comment == models.Comment.id,
                                                models.Like.fk_user == id,
                                                id is not None), isouter=True)\
                            .join(models.Book, models.Book.id == models.Rate.fk_book)\
                            .order_by(models.Comment.date.desc())\
                            .offset(page * 8).limit(8).all()
                            
        sort = rates
        sort.append(comments[0]) if comments else None
        sort = sorted(sort, key = lambda x: x[0], reverse=True)
        query = {'data': sort}
        
        aux = []
        for x in query['data']:

                query_count = self.session.query(func.count(models.Comment.id).label('count_comments'))\
                                    .where(models.Comment.fk_rate == x.id_rate).all()

                book = get_and_format_output(x['identifier'])
                book.update({'id': x['id_book']})
                aux.append({
                    'rates': query_count[0]['count_comments'],
                    'type': x.type,
                    'id': x.id_rate,
                    'date': x.formatted_date,
                    'text': x.text if len(x.text) < 250 else x.text[:250] + "...",
                    'rate': x.rate if x.type == 'r' else 0,
                    'you_liked': True if x.like_id else False,
                    'likes': x.likes,
                    'user': {
                        'nickname': x.nickname,
                        'photo': x.photo,
                        'id': x.id_user
                    },
                    'book': book
                })
        return aux
