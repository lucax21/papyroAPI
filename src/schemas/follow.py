from pydantic import BaseModel, HttpUrl
from src.schemas.user import UserSuperBasic
from typing import Optional

class Follow(UserSuperBasic):
	pass
    # id: int
    # nickname: str
    # photo: Optional[HttpUrl] = 'https://i.pinimg.com/736x/67/4f/c5/674fc554838de6abdbf274bdc0ca446c.jpg'