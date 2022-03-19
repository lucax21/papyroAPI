#Representação do banco de dados
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Text, Boolean, Table
from sqlalchemy.orm import relationship
from src.db.database import Base


usuario_genero = Table("usuario_genero", Base.metadata,
                        Column("fk_genero", ForeignKey("genero.id"), primary_key=True),
                        Column("fk_usuario", ForeignKey("usuario.id"), primary_key=True)
                    )


# class UsuarioGenero(Base):
#     __tablename__ = 'usuario_genero'

#     fk_genero = Column('fk_genero',ForeignKey('genero.id'), primary_key=True)
#     fk_usuario = Column('fk_usuario',ForeignKey('usuario.id'), primary_key=True)
   
#     # genero = relationship('Genero')
#     genero = relationship('Genero', back_populates='usuarios')
#     usuario = relationship('Usuario', back_populates='generos')


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String(255), unique=True)
    nome = Column(String(255))
    apelido = Column(String(30), unique=True)
    descricao = Column(Text)
    senha = Column(String(256))
    data_nascimento = Column(DateTime)
    foto = Column(String(255), nullable=True)

    ativo = Column(Boolean, default=False)
    confirmacao = Column(UUID(as_uuid=True), nullable=True, default=uuid.uuid4)

    # generos = relationship('UsuarioGenero', back_populates="usuario")
    # generos = relationship('UsuarioGenero')

    generos = relationship("Genero", secondary=usuario_genero, back_populates='usuarios')
    # grupos = relationship("UsuarioGrupo", back_populates='usuario')
    grupos = relationship("Grupo", secondary='usuario_grupo', back_populates='usuarios')

    livros_lidos = relationship("Livro", 
                                                    secondary='join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                                    # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                                    # ,
                                                    ,primaryjoin="and_(StatusUsuarioLivro.status=='Lido(s)')"
                                                    # secondaryjoin="UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status"
                                                    ,uselist=True,
                                                    viewonly=True
                                                    )
    livros_lerei = relationship("Livro", 
                                                    secondary='join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                                    # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                                    # ,
                                                    ,primaryjoin="and_(StatusUsuarioLivro.status=='Lerei')"
                                                    # secondaryjoin="UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status"
                                                    ,uselist=True,
                                                    viewonly=True
                                                    )
    livros_lendo = relationship("Livro", 
                                                    secondary='join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                                    # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                                    # ,
                                                    ,primaryjoin="and_(StatusUsuarioLivro.status=='Lendo')"
                                                    # secondaryjoin="UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status"
                                                    ,uselist=True,
                                                    viewonly=True
                                                    )

class Genero(Base):
    __tablename__ = 'genero'

    id = Column(Integer, primary_key=True, index=True)

    genero = Column(String(100))

    # usuarios = relationship("UsuarioGenero", secondary="usuario_genero")
    # usuarios = relationship("UsuarioGenero", back_populates="genero")

    usuarios = relationship("Usuario", secondary=usuario_genero, back_populates="generos")


class Livro(Base):
    __tablename__ = 'livro'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(255))
    ano = Column(Date)
    nota = Column(Integer)
    sinopse = Column(Text)
    capa = Column(String(255), nullable=True)

    fk_genero = Column(Integer, ForeignKey('genero.id'))

    # usuarios = relationship("Usuario", secondary='usuario_livro', back_populates="livros_lidos")


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

    isbn = Column(String(13), primary_key=True)

    fk_livro = Column(Integer, ForeignKey('livro.id'))

class Grupo(Base):
    __tablename__ = 'grupo'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(100))
    foto = Column(String(255))
    descricao = Column(String(1023))

    # usuarios = relationship("UsuarioGrupo", back_populates="grupo")
    usuarios = relationship("Usuario",secondary="usuario_grupo", back_populates="grupos")


class Cargo(Base):
    __tablename__ = 'cargo'

    id = Column(Integer, primary_key=True, index=True)

    cargo = Column(String(127))

class UsuarioGrupo(Base):
    __tablename__ = 'usuario_grupo'

    fk_grupo = Column(ForeignKey("grupo.id"), primary_key=True)
    fk_usuario = Column(ForeignKey("usuario.id"), primary_key=True)
    fk_cargo = Column(ForeignKey("cargo.id"))
    data_entrada = Column(Date)

    # grupos = relationship("Grupo", back_populates="usuarios")
    # usuarios = relationship("Usuario", back_populates="grupos")

class StatusUsuarioLivro(Base):
    __tablename__= 'status_usuario_livro'

    id = Column(Integer, primary_key=True, index=True)

    status = Column(String(100))

    # stat = relationship('UsuarioLivro', back_populates="status")
    
class UsuarioLivro(Base):
    __tablename__ = 'usuario_livro'

    fk_livro = Column(ForeignKey("livro.id"), primary_key=True)
    fk_usuario = Column(ForeignKey("usuario.id"), primary_key=True)
    fk_status = Column(ForeignKey("status_usuario_livro.id"))
    data_entrada = Column(Date)

    # status = relationship("StatusUsuarioLivro", back_populates="stat")
    