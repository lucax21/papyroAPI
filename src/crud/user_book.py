from fastapi import HTTPException, status
from sqlalchemy import and_, update, insert, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.db.models import models
from sqlalchemy.sql.functions import func
from src.utils.enum.reading_type import ReadingTypes
from src.utils.format_book_output import get_and_format_output


class CrudUserBook:

    def __init__(self, session: Session):
        self.session = session

    
    def book_user_status(self, id_user: int, id_status: int, id_book):
            

            query = self.session.query(models.UserBook) \
                .where(and_(models.UserBook.fk_user == id_user, models.UserBook.fk_book == id_book)).first()
            
            if query and id_status == 0:
                stmt = (delete(models.UserBook).
                         where(and_(models.UserBook.fk_user == id_user, models.UserBook.fk_book == id_book)))

                try:
                    self.session.execute(stmt)
                    self.session.commit()

                    return {'id_book': id_book, 'id_status': id_status, 'id_user': id_user}
                except IntegrityError as err:
                    self.session.rollback()
                    print(err)
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao adicionar um novo status.")

            # update
            elif query:
                stmt = update(models.UserBook) \
                    .where(and_(models.UserBook.fk_user == id_user,
                                models.UserBook.fk_book == id_book)) \
                    .values(fk_book=id_book,
                            fk_user=id_user,
                            fk_status=id_status,
                            date=func.now()
                            )
                try:
                    self.session.execute(stmt)
                    self.session.commit()

                    return {'id_book': id_book, 'id_status': id_status, 'id_user': id_user}
                except IntegrityError as err:
                    self.session.rollback()
                    print(err)
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao alterar um novo status.")
            
            # insert
            else:
                if id_status != 0:
                    stmt = insert(models.UserBook).values(fk_book=id_book,
                                                        fk_user=id_user,
                                                        fk_status=id_status,
                                                        date=func.now()
                                                        )
                    try:
                        self.session.execute(stmt)
                        self.session.commit()

                        return {'id_book': id_book, 'id_status': id_status, 'id_user': id_user}
                    except IntegrityError as err:
                        self.session.rollback()
                        print(err)
                        raise HTTPException(status_code=status.http_400_bad_request, detail="erro ao adicionar um novo status.")
                


    def get_companionship(self, id_book: int):
        readers_reading = self.session.query(models.User.id.label('id'),
                                             models.User.nickname,
                                             models.User.photo,
                                             ) \
            .where(and_(models.UserBook.fk_book == id_book, models.UserBook.fk_status == ReadingTypes.READING)) \
            .join(models.UserBook, models.UserBook.fk_user == models.User.id) \
            .limit(16).all()
        readers_read = self.session.query(models.User.id.label('id'),
                                          models.User.nickname,
                                          models.User.photo,
                                          ) \
            .where(and_(models.UserBook.fk_book == id_book, models.UserBook.fk_status == ReadingTypes.READ)) \
            .join(models.UserBook, models.UserBook.fk_user == models.User.id) \
            .limit(16).all()
        readers_to_read = self.session.query(models.User.id.label('id'),
                                             models.User.nickname,
                                             models.User.photo,
                                             ) \
            .where(and_(models.UserBook.fk_book == id_book, models.UserBook.fk_status == ReadingTypes.TO_READ)) \
            .join(models.UserBook, models.UserBook.fk_user == models.User.id) \
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
    

    def get_companionship_status(self, id_book: int, id_status: int, page: int):
        query = self.session.query(models.User.id.label('id'),
                                   models.User.nickname,
                                   models.User.photo,
                                   ) \
            .where(and_(models.UserBook.fk_book == id_book, models.UserBook.fk_status == id_status)) \
            .join(models.UserBook, models.UserBook.fk_user == models.User.id) \
            .offset(page * 20).limit(20).all()
        query_status = self.session.query(models.Status).where(models.Status.id == id_status).first()

        return {

            'id': id_status,
            'status': query_status.status if query_status.status else 'Erro, status inexistente.',
            'readers': query

        }

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
                'rate': x['sum'] / x['count'] if x['count'] > 0 else 0,
                'id': x['id']
            })
            return book

        if len(data) > 0:
            book = list(map(arrange_book, data))
            return book

        return None