from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status
from src.db.models import models

from src.schemas.rate import NewRate

from sqlalchemy.sql.functions import func

class CrudRate():
    def __init__(self, session: Session):
        self.session = session


    def new_rate(self, id_user:int, data: NewRate):
        
        try:
            stmt = models.Rate(fk_user=id_user, fk_book=data.id_book, text=data.text, rate=data.rate, likes=0, date=func.now())
            self.session.add(stmt)
            self.session.commit()
            return 1
        except Exception:
            self.session.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
