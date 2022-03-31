from __future__ import annotations

from pydantic import BaseModel

class ComentarioSalvar(BaseModel):
    id_livro: int
    id_avaliacao: int
    texto: str
    nota: int