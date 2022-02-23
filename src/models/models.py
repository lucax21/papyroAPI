#Representação do banco de dados
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Text, Boolean, Table
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

    ativo = Column(Boolean, default=False)
    confirmacao = Column(UUID(as_uuid=True), nullable=True, default=uuid.uuid4)

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


class Livro(Base):
    __tablename__ = 'livro'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(255))
    ano = Column(Date)
    nota = Column(Integer)
    sinopse = Column(Text)
    capa = Column(String(255), nullable=True)

    fk_genero = Column(Integer, ForeignKey('genero.id'))

class Autor(Base):
    __tablename__ = 'autor'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(255))

class Papel(Base):
    __tablename__ = 'papel'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(255))

class LivroAutores(Base):
    __tablename__ = 'livro_autores'

    fk_autor = Column(Integer, ForeignKey('autor.id'), primary_key=True)
    fk_livro = Column(Integer, ForeignKey('livro.id'), primary_key=True)
    fk_papel = Column(Integer, ForeignKey('papel.id'))

class LivroISBN(Base):
    __tablename__ = 'livro_isbn'

    isbn = Column(String(10), primary_key=True)

    fk_livro = Column(Integer, ForeignKey('livro.id'))

