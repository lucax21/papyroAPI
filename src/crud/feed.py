from statistics import mode
from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func
from src.db.models import models
from src.utils.format_book_output import get_and_format_output


class CrudFeed:

    def __init__(self, session: Session):
        self.session = session

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
        # query = self.session.query( 
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
        #                     .join(models.Rate, models.Rate.id == models.Comment.fk_rate, isouter=True)\
        #                     .join(models.Like, and_(models.Like.fk_rate == models.Rate.id,
        #                                 models.Like.fk_user == id,
        #                                 id is not None), isouter=True)\
        #                     .join(models.Book, models.Book.id == models.Rate.fk_book)\
        #                     .order_by(models.Rate.date.desc())\
        #                     .offset(page * 20).limit(20).all()

        rates = self.session.query(models.User.id.label('id_user'),
                                   models.User.nickname.label('nickname'),
                                   models.User.photo.label('photo'),
                                   models.Rate.id.label('id_rate'),
                                   models.Rate.text.label('text'),
                                   models.Rate.rate.label('rate'),
                                   models.Rate.likes.label('likes_rate'),
                                   models.Rate.date.label('date_rate'),
                                   models.Book.id.label('id_book'),
                                   models.Book.identifier.label('identifier'),
                                   models.Like.id.label('like_id'),
                                   )\
                    .where(and_(
                                models.Friend.fk_origin==id,
                                # models.Friend.pending==False,
                                # models.Friend.ignored==False
                                ))\
                    .join(models.Friend, models.User.id == models.Friend.fk_destiny)\
                    .join(models.Rate, models.User.id == models.Rate.fk_user)\
                    .join(models.Like, and_(models.Like.fk_rate == models.Rate.id,
                                        models.Like.fk_user == id,
                                        id is not None), isouter=True)\
                    .join(models.Book, models.Book.id == models.Rate.fk_book)\
                    .all()
        
        comments = self.session.query(models.User.id.label('id_user'),
                                    models.User.nickname.label('nickname'),
                                    models.User.photo.label('photo'),
                                    models.Comment.id.label('id_comment'),
                                    models.Comment.text,
                                    models.Comment.likes,
                                    models.Comment.date,
                                    models.Book.id.label('id_book'),
                                    models.Book.identifier.label('identifier'),
                                    )\
                                .where(and_(
                                    models.Friend.fk_origin==id,
                                # models.Friend.pending==False,
                                # models.Friend.ignored==False
                                ))\
                                .join(models.Friend, models.User.id == models.Friend.fk_destiny)\
                                .join(models.Comment, models.User.id == models.Comment.fk_user)\
                                .join(models.Book, models.Book.id == models.Comment.fk_book)\
                                .all()
        return rates

        # a = {'data': }
        # list(a.keys()).sort()

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