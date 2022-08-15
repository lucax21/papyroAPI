from sqlalchemy import and_
from sqlalchemy.orm import Session
from src.db.models import models

class CrudNotification:

    def __init__(self, session: Session):
        self.session = session

    def notification(self, id_user: int, page: int):
        rates = self.session.query(models.Rate.date,
                                    models.Rate.id,
                                    models.Rate.
                                    )\
                        .where()\
                        .join()

