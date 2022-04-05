#Representação do banco de dados
from turtle import back
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Text, Boolean, Table
from sqlalchemy.orm import relationship
from src.db.database import Base
from sqlalchemy.ext.associationproxy import association_proxy

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

    lendoss = relationship("UsuarioLivro", back_populates='usuario')
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

    usuario_avaliacao = relationship("Avaliacao", back_populates="usuario")
    # amigos = relationship("Amigo", back_populates="usuario_origem")
    amigos = relationship('Amigo', backref='Amigo.fk_destino',primaryjoin='Usuario.id==Amigo.fk_origem', lazy='dynamic')
    mensagens = relationship('Mensagem', backref='Mensagem.fk_destino',primaryjoin='Usuario.id==Mensagem.fk_origem', lazy='dynamic')

class Genero(Base):
    __tablename__ = 'genero'

    id = Column(Integer, primary_key=True, index=True)

    genero = Column(String(100))

    usuarios = relationship("Usuario", secondary=usuario_genero, back_populates="generos")
    generos = relationship("Livro", back_populates="genero")

class Livro(Base):
    __tablename__ = 'livro'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(255))
    ano = Column(Date)
    nota = Column(Integer)
    sinopse = Column(Text)
    capa = Column(String(255), nullable=True)

    fk_genero = Column(Integer, ForeignKey('genero.id'))

    autores = relationship("LivroAutores", back_populates="livro")
    livros_lendo = relationship("UsuarioLivro", back_populates="livro_lendo")
    status_usuario_livro = relationship("StatusUsuarioLivro", 
                                        secondary='join(UsuarioLivro, Livro, UsuarioLivro.fk_status == Livro.id)'
                                        # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                        # ,
                                        # ,primaryjoin="and_(UsuarioLivro.fk_status==1)"
                                        # ,primaryjoin="and_(Livro.id == UsuarioLivro.fk_livro, UsuarioLivro.fk_usuario==Usuario.id)"
                                        ,secondaryjoin="UsuarioLivro.fk_status == StatusUsuarioLivro.id"
                                        ,uselist=True,
                                        viewonly=True
                                        )
    test = relationship("UsuarioLivro", back_populates="test1")
    test2 = relationship("Autor", 
                                                    secondary='join(LivroAutores, Autor, Autor.id == LivroAutores.fk_autor)'
                                                    # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                                    # ,
                                                    # ,primaryjoin="and_(StatusUsuarioLivro.status=='Lendo')"
                                                    # secondaryjoin="UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status"
                                                    ,uselist=True,
                                                    viewonly=True
                                                    )
    usuario = relationship("Usuario", 
                                                    secondary='join(UsuarioLivro, Usuario, Usuario.id == UsuarioLivro.fk_usuario)'
                                                    # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
                                                    # ,
                                                    # ,primaryjoin="and_(StatusUsuarioLivro.status=='Lendo')"
                                                    # secondaryjoin="UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status"
                                                    ,uselist=True,
                                                    viewonly=True
                                                    )
    
    genero = relationship("Genero", back_populates="generos")
    avaliacoes = relationship("Avaliacao", back_populates="avaliacao")

class Autor(Base):
    __tablename__ = 'autor'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(255))

    livros = relationship("LivroAutores", back_populates="autor")

class Papel(Base):
    __tablename__ = 'papel'

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(255))

class LivroAutores(Base):
    __tablename__ = 'livro_autores'

    fk_autor = Column(Integer, ForeignKey('autor.id'), primary_key=True)
    fk_livro = Column(Integer, ForeignKey('livro.id'), primary_key=True)
    fk_papel = Column(Integer, ForeignKey('papel.id'))

    livro = relationship("Livro", back_populates="autores")
    autor = relationship("Autor", back_populates="livros")


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

    # livro_status = relationship('UsuarioLivro', back_populates="status")

    livros = relationship("UsuarioLivro", back_populates="statuss")  


class UsuarioLivro(Base):
    __tablename__ = 'usuario_livro'

    fk_livro = Column(ForeignKey("livro.id"), primary_key=True)
    fk_usuario = Column(ForeignKey("usuario.id"), primary_key=True)
    fk_status = Column(ForeignKey("status_usuario_livro.id"))
    data_entrada = Column(Date)

    livro_lendo = relationship("Livro", back_populates="livros_lendo")
    usuario = relationship("Usuario", back_populates="lendoss")

    statuss = relationship("StatusUsuarioLivro", back_populates="livros")
    test1 = relationship("Livro", back_populates="test")

class Avaliacao(Base):
    __tablename__ = 'avaliacao'

    id = Column(Integer, primary_key=True, index=True)

    texto = Column(String(255))
    data_criacao = Column(DateTime)
    nota = Column(Integer)
    likes = Column(Integer)

    fk_usuario = Column(ForeignKey("usuario.id"))
    fk_livro = Column(ForeignKey("livro.id"))

    avaliacao = relationship("Livro", back_populates="avaliacoes")
    usuario = relationship("Usuario", back_populates="usuario_avaliacao")
    comentarios = relationship("Likes", back_populates="avaliacao")


class Comentario(Base):
    __tablename__ = 'comentario'

    id = Column(Integer, primary_key=True, index=True)    

    nota = Column(Integer)
    texto = Column(String(255))
    data_criacao = Column(DateTime)
    likes = Column(Integer)

    fk_usuario = Column(ForeignKey("usuario.id"))
    fk_livro = Column(ForeignKey("livro.id"))

    avaliacoes = relationship("Likes", back_populates="comentario")

class   Likes(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, index=True)

    fk_comentario = Column(ForeignKey("comentario.id"))
    fk_avaliacao = Column(ForeignKey("avaliacao.id"))
    fk_usuario = Column(ForeignKey("usuario.id"))

    avaliacao = relationship("Avaliacao", back_populates="comentarios")
    comentario = relationship("Comentario", back_populates="avaliacoes")

class Amigo(Base):
    __tablename__ = 'amigo'

    fk_origem = Column(ForeignKey("usuario.id"), primary_key=True)
    fk_destino = Column(ForeignKey("usuario.id"), primary_key=True)

    pendente = Column(Boolean)
    ignorado = Column(Boolean)

    usuario_origem = relationship("Usuario", foreign_keys='Amigo.fk_origem')
    usuario_destino = relationship("Usuario", foreign_keys='Amigo.fk_destino')

class Mensagem(Base):
    __tablename__ = 'mensagem'

    id = Column(Integer, primary_key=True, index=True)

    texto = Column(String(255), nullable=False)
    data_criacao = Column(DateTime)

    fk_origem = Column(ForeignKey("usuario.id"))
    fk_destino = Column(ForeignKey("usuario.id"))

    usuario_origem = relationship("Usuario", foreign_keys='Mensagem.fk_origem')
    usuario_destino = relationship("Usuario", foreign_keys='Mensagem.fk_destino')