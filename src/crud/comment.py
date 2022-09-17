from sqlalchemy.orm import Session

from src.db.models.models import *


class CrudComment:
    def __init__(self, session: Session):
        self.session = session

    def new_comment(self, data, user_id):
        stmt = Comment(fk_user=user_id, date=func.now(), text=data.text, likes=0, fk_rate=data.rate_id)
        self.session.add(stmt)
        self.session.commit()
        self.session.refresh(stmt)
        return {'comment_id': stmt.id}
