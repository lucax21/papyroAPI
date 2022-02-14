#Representação do banco de dados

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String(255), unique=True)
    nome = Column(String(255))
    apelido = Column(String(30), unique=True)
    senha = Column(String(256))
    data_nascimento = Column(DateTime)
    foto = Column(String(255), nullable=True)

    genero = relationship('Genero', secondary='usuario_genero')

class Genero(Base):
    __tablename__ = 'genero'

    id = Column(Integer, primary_key=True, index=True)

    genero = Column(String(100))

    Usuario = relationship(Usuario, secondary='usuario_genero')

class UsuarioGenero(Base):
    __tablename__ = 'usuario_genero'

    fk_genero = Column(Integer, ForeignKey('genero.id'), primary_key=True)
    fk_usuario = Column(Integer, ForeignKey('usuario.id'), primary_key=True)

