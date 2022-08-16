from sqlalchemy import and_
from sqlalchemy.orm import Session
from src.db.models import models
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.expression import literal
from src.utils.format_book_output import get_and_format_output

class CrudNotification:

    def __init__(self, session: Session):
        self.session = session

    def notification(self, id_user: int, page: int):
      
        rates = self.session.query(
                                    models.Comment.date.label('data'),
                                    models.Comment.id.label('id_comment'),
                                    models.Comment.formatted_date,
                                    models.Rate.id.label('id_rate'),
                                    models.Book.id.label('id_book'),
                                    models.Book.identifier,
                                    models.User.nickname,
                                    models.User.photo,
                                    models.User.id,
                                    literal('r').label('type'),
                                    func.concat(models.User.nickname, ' comentou ', ' "', func.substring(models.Comment.text, 1,12),'... "', ' na sua avaliação.').label('text'),
                                    )\
                            .join(models.Comment, models.Comment.fk_rate == models.Rate.id)\
                            .join(models.Book, models.Book.id == models.Rate.fk_book)\
                            .join(models.User, models.User.id == models.Comment.fk_user)\
                            .order_by(models.Rate.date.desc(), models.Comment.date.desc())\
                            .offset(page * 4).limit(4).all()
        
        pending = self.session.query(
                                        models.Friend.date.label('data'),
                                        models.Friend.pending,
                                        models.Friend.formatted_date,
                                        models.User.id, models.User.nickname, models.User.photo,
                                        literal('p').label('type'),
                                        func.concat(models.User.nickname, ' pediu para seguir você.').label('text'),
                                    )\
                                    .where(and_(models.Friend.fk_destiny == id_user,
                                                models.Friend.ignored == False,
                                                models.Friend.pending == True,
                                                ))\
                                    .join(models.Friend, models.User.id == models.Friend.fk_origin)\
                                    .order_by(models.Friend.date.desc())\
                                    .offset(page * 4).limit(4).all()
        
        accept = self.session.query(
                                        models.Friend.date.label('data'),
                                        models.Friend.pending,
                                        models.Friend.formatted_date,
                                        models.User.id, models.User.nickname, models.User.photo,
                                        literal('a').label('type'),
                                        func.concat(models.User.nickname, ' aceitou sua solicitação.').label('text'),
                                    )\
                                    .where(and_(models.Friend.fk_origin == id_user,
                                                models.Friend.ignored == False,
                                                models.Friend.pending == False,
                                                ))\
                                    .join(models.Friend, models.User.id == models.Friend.fk_destiny)\
                                    .order_by(models.Friend.date.desc())\
                                    .offset(page * 4).limit(4).all()
                           
        likes = self.session.query(
                                    models.Like.date.label('data'),
                                    models.Like.id,
                                    models.Like.formatted_date,
                                    models.Rate.id.label('id_rate'),
                                    models.Book.id.label('id_book'),
                                    models.Book.identifier,
                                    models.User.nickname,
                                    models.User.photo,
                                    models.User.id.label('id_user'),
                                    literal('l').label('type'),
                                    func.concat(models.User.nickname, ' curtiu sua avaliação sobre o livro.').label('text'),
                                    )\
                            .where(models.Rate.fk_user == id_user)\
                            .join(models.Like, models.Like.fk_rate == models.Rate.id)\
                            .join(models.Book, models.Book.id == models.Rate.fk_book)\
                            .join(models.User, models.User.id == models.Like.fk_user)\
                            .order_by(models.Like.date.desc())\
                            .offset(page * 4).limit(4).all()
        

        sort = rates
        sort.append(pending[0])
        sort.append(accept[0])
        sort.append(likes[0])

        sort = sorted(sort, key = lambda x: x[0], reverse=True)
        data = {'data': sort}

        aux = []
        for x in data['data']:
            aux.append({
                    'book': get_and_format_output(x.identifier) if x.type == 'l' else None,
                    'user': {
                            'id': x.id,
                            'photo': x.photo,
                            'nickname': x.nickname,
                        },
                    'notification': {
                            'id': x.id_rate if x.type == 'r' else None,
                            'date': x.formatted_date,
                            'type': x.type,
                            'text': x.text,
                        }
                })
    
        return aux
