from sqlalchemy import and_
from sqlalchemy.orm import Session
from src.db.models import models

class CrudFriend:

    def __init__(self, session: Session):
        self.session = session

    def get_friends(self, id: int, page: int):
        data = self.session.query(models.User.id, models.User.nickname, models.User.photo)\
                .where(and_(models.Friend.fk_origin == id,
                            #models.Friend.pending == False,
                            #models.Friend.ignored == False
                            ))\
                .join(models.Friend, models.User.id == models.Friend.fk_destiny)\
                .offset(page * 8).limit(8).all()
        return data

