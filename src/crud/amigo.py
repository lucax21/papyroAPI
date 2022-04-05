from sqlalchemy.orm import Session, joinedload

from src.db.models import models
from typing import List

class CrudAmigo():
    def __init__(self, session: Session):
        self.session = session
