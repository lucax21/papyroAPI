from fastapi import HTTPException, status
from sqlalchemy import and_, update
from sqlalchemy.orm import Session
from src.db.models import models

class CrudFriend:

    def __init__(self, session: Session):
        self.session = session

    def get_friends(self, id: int, friend_type: str, page: int):
        
        if friend_type == "following":
            return self.session.query(models.User.id, models.User.nickname, models.User.photo)\
                .where(and_(models.Friend.fk_origin == id,
                            models.Friend.pending == False,
                            models.Friend.ignored == False
                            ))\
                .join(models.Friend, models.User.id == models.Friend.fk_destiny)\
                .offset(page * 16).limit(16).all()
        if friend_type == "followers":
            return self.session.query(models.User.id, models.User.nickname, models.User.photo)\
                .where(and_(models.Friend.fk_destiny == id,
                            models.Friend.pending == False,
                            models.Friend.ignored == False
                            ))\
                .join(models.Friend, models.User.id == models.Friend.fk_origin)\
                .offset(page * 16).limit(16).all()
    
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passe o parâmetro de leitura.")

    def accept_or_ignored_friend(self, id_user, oper_type, mode, id_friend):
        if oper_type == 'a':
            update_friend = update(models.Friend).values(pending=mode).where(and_(models.Friend.fk_origin == id_friend, models.Friend.fk_destiny == id_user))
            self.session.execute(update_friend)
            self.session.commit()
            return 1
        if oper_type == 'i':
            update_friend = update(models.Friend).values(ignored=mode).where(and_(models.Friend.fk_origin == id_friend, models.Friend.fk_destiny == id_user))
            self.session.execute(update_friend)
            self.session.commit()
            return 1

    def add_friend(self, id_user, id_friend):
        try:
            stmt = models.Friend(fk_origin=id_user, fk_destiny=id_friend, pending=True, ignored = False)
            self.session.add(stmt)
            self.session.commit()
            return 1
        except Exception:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao adicionar amigo.")
