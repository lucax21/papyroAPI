from fastapi import HTTPException, status
from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.db.models import models


class CrudFollow:

    def __init__(self, session: Session):
        self.session = session

    def get_follow(self, id: int, follow_type: str, page: int):

        if follow_type == "following":
            return self.session.query(models.User.id, models.User.nickname, models.User.photo) \
                .where(and_(models.Friend.fk_origin == id)) \
                .join(models.Friend, models.User.id == models.Friend.fk_destiny) \
                .offset(page * 16).limit(16).all()
        if follow_type == "followers":
            return self.session.query(models.User.id, models.User.nickname, models.User.photo) \
                .where(and_(models.Friend.fk_destiny == id)) \
                .join(models.Friend, models.User.id == models.Friend.fk_origin) \
                .offset(page * 16).limit(16).all()

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passe o parâmetro de leitura.")


    def add_remove_follow(self, id_user, id_follow, mode):
        user_obj = self.session.query(models.Friend)\
            .where(and_(models.Friend.fk_origin == id_user, models.Friend.fk_destiny == id_follow)).first()
        stmt = models.Friend(fk_origin=id_user, fk_destiny=id_follow)
        if mode and not user_obj:
            self.session.add(stmt)
            self.session.commit()
            return 1
        if not mode and user_obj:
            self.session.delete(user_obj)
            self.session.commit()
            return -1
        
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Operação inválida.")

