from pydantic import BaseModel, validator, constr
from typing import Optional
from fastapi import HTTPException, status

class NewRate(BaseModel):
    id_book: int
    text: Optional[constr(max_length=5000)] = None
    rate: int

    @validator('rate')
    def vl_rate(cls, value):
        if value < 0 or value > 5:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Somente valores entre 0 e 5.")
        return value
