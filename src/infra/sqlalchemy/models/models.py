#Representação do banco de dados

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String, unique=True)
    nome = Column(String)
    apelido = Column(String)
    senha = Column(String)
    data_nascimento = Column(DateTime)
    foto = Column(String)
