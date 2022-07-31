from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.db.models.models import Like


class CrudLike:
    def __init__(self, session: Session):
        self.session = session

    def like_by_id(self, id, like_type, user_id, mode):
        if like_type == 'r':
            like_obj = self.session.query(Like).where(and_(Like.fk_user == user_id, Like.fk_rate == id)).first()
            stmt = Like(fk_rate=id, fk_user=user_id)
            if mode and not like_obj:
                self.session.add(stmt)
                self.session.commit()
                self.session.refresh(stmt)
                return {'id': stmt.id}

            if not mode and like_obj:
                self.session.delete(like_obj)
                self.session.commit()
                return {'id': -1}

        if like_type == 'c':
            like_obj = self.session.query(Like).where(and_(Like.fk_user == user_id, Like.fk_comment == id)).first()
            stmt = Like(fk_comment=id, fk_user=user_id)
            if mode and not like_obj:
                self.session.add(stmt)
                self.session.commit()
                self.session.refresh(stmt)
                return {'id': stmt.id}

            if not mode and like_obj:
                self.session.delete(like_obj)
                self.session.commit()
                return {'id': -1}
