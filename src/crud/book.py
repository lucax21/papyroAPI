from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func

from src.db.models import models
from src.external_api.get_book import get_by_identifier
from src.utils.enum.reading_type import ReadingTypes
from src.utils.format_book_output import format_book_output


class CrudBook:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id, page, user_id):

        data = self.session.query(models.Book.identifier,
                                  func.count(models.Rate.id).label('count'),
                                  func.sum(models.Rate.rate).label('sum')) \
            .where(models.Book.id == id) \
            .join(models.Rate, models.Rate.fk_book == models.Book.id, isouter=True) \
            .group_by(models.Book).first()

        rating_new_format = []
        if data.count > 0:
            rates = self.session.query(models.Rate.text,
                                       models.Rate.formatted_date,
                                       models.Rate.likes,
                                       models.Rate.id,
                                       models.User.photo,
                                       models.Rate.rate,
                                       models.User.id.label('user_id'),
                                       models.User.nickname,
                                       models.Like.id.label('like_id'),
                                       func.count(models.Comment.id).label('comments')) \
                .where(models.Rate.fk_book == id) \
                .join(models.User, models.Rate.fk_user == models.User.id) \
                .join(models.Like, and_(models.Like.fk_rate == models.Rate.id,
                                        models.Like.fk_user == user_id,
                                        user_id is not None), isouter=True)\
                .join(models.Comment, models.Comment.fk_rate == models.Rate.id, isouter=True) \
                .group_by(models.Rate.text,
                          models.Rate.formatted_date,
                          models.Rate.likes,
                          models.Rate.id,
                          models.User.photo,
                          models.Rate.rate,
                          models.User.id.label('user_id'),
                          models.User.nickname,
                          models.Like.id.label('like_id'))\
                .offset(page * 20).limit(20).all()

            for rate in rates:
                rating_new_format.append({
                    'date': rate.formatted_date,
                    'id': rate.id,
                    'likes': rate.likes,
                    'rate': rate.rate,
                    'you_like': rate.like_id is not None,
                    'text': rate.text,
                    'comments': rate.comments,
                    'user': {
                        'nickname': rate.nickname,
                        'photo': rate.photo,
                        'id': rate.user_id
                    }
                })

        user = self.session.query(models.UserBook.fk_status) \
            .where(and_(models.UserBook.fk_book == id,
                        models.UserBook.fk_user == user_id))\
            .first()

        people_reading = self.session.query(func.count(models.UserBook.fk_user).label('users'))\
            .where((models.UserBook.fk_status == ReadingTypes.READING)).first()

        book = get_by_identifier(data.identifier)

        if "volumeInfo" not in book:
            raise HTTPException(status_code=404, detail='Não encontrado')

        book = format_book_output(book)

        if isinstance(book, str):
            raise HTTPException(status_code=400, detail=book)

        book.update({
            'id': id,
            'status': user.fk_status if user else None,
            'rate': data.sum / data.count if data.count > 0 else None,
            'raters': data.count,
            'reviews': rating_new_format,
            'company': people_reading.users if people_reading else 0
        })

        return book

    #
    # def avaliar_livro(self, id_user, ava: LivroAvaliar):
    #     try:
    #         stmt = insert(models.Avaliacao).values(fk_livro=ava.id_livro,
    #                                                fk_usuario=id_user,
    #                                                nota=ava.nota,
    #                                                texto=ava.texto,
    #                                                likes=0,
    #                                                data_criacao=func.now()
    #                                                )
    #         self.session.execute(stmt)
    #         self.session.commit()
    #         return 1
    #     except Exception as error:
    #         self.session.rollback()
    #         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
