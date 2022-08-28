from sqlalchemy import and_, update
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import func

from src.db.models.models import Like, Rate, Comment


class CrudLike:
    def __init__(self, session: Session):
        self.session = session

    def like_by_id(self, id, like_type, user_id, mode):
        
        if like_type == 'r':
            like_obj = self.session.query(Like).where(and_(Like.fk_user == user_id, Like.fk_rate == id)).first()
            stmt = Like(fk_rate=id, fk_user=user_id, date=func.now())
            if mode and not like_obj:
                query_rate = self.session.query(Rate.likes).where(Rate.id == id).first()
                update_rate = update(Rate).values(likes=query_rate['likes']+1).where(Rate.id==id)
                self.session.execute(update_rate)
                
                self.session.add(stmt)
                self.session.commit()
                self.session.refresh(stmt)
                
                return {'id': stmt.id}

            if not mode and like_obj:
                query_rate = self.session.query(Rate.likes).where(Rate.id == id).first()
                update_rate = (update(Rate).values(likes=query_rate['likes']-1).where(Rate.id==id))
                self.session.execute(update_rate)

                self.session.delete(like_obj)
                self.session.commit()
                
                return {'id': -1}

        if like_type == 'c':
            like_obj = self.session.query(Like).where(and_(Like.fk_user == user_id, Like.fk_comment == id)).first()
            stmt = Like(fk_comment=id, fk_user=user_id, date=func.now())
            if mode and not like_obj:
                query_comment = self.session.query(Comment.likes).where(Comment.id == id).first()
                update_comment = (update(Comment).values(likes=query_comment['likes']+1).where(Comment.id == id))
                self.session.execute(update_comment)
                self.session.add(stmt)
                self.session.commit()
                self.session.refresh(stmt)
                return {'id': stmt.id}

            if not mode and like_obj:
                query_comment = self.session.query(Comment.likes).where(Comment.id == id).first()
                update_comment = (update(Comment).values(likes=query_comment['likes']-1).where(Comment.id == id))
                self.session.execute(update_comment)

                self.session.delete(like_obj)
                self.session.commit()
                return {'id': -1}
