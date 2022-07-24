#Representação do banco de dados
from turtle import back
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func, Column, Integer, String, DateTime, ForeignKey, Date, Text, Boolean, Table
from sqlalchemy.orm import relationship
from src.db.database import Base
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.orm import column_property

user_genre = Table("user_genre", Base.metadata,
                        Column("fk_genre", ForeignKey("genre.id"), primary_key=True),
                        Column("fk_user", ForeignKey("user.id"), primary_key=True)
                    )


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String(255), unique=True)
    name = Column(String(255))
    nickname = Column(String(30), unique=True)
    description = Column(Text)
    password = Column(String(256))
    birthday = Column(Date)
    photo = Column(String(255), nullable=True)
    active = Column(Boolean, default=False)
    confirmation = Column(UUID(as_uuid=True), nullable=True, default=uuid.uuid4)
    formatted_birthday = column_property(func.to_char(birthday, 'DD/MM/YYYY'))
    
    genres = relationship("Genre", secondary=user_genre, back_populates='users')
    # lendoss = relationship("UsuarioLivro", back_populates='usuario')
    # livros_lidos = relationship("Livro", 
    #                                                 secondary='join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
    #                                                 # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
    #                                                 # ,
    #                                                 ,primaryjoin="and_(StatusUsuarioLivro.status=='Lido(s)')"
    #                                                 # secondaryjoin="UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status"
    #                                                 ,uselist=True,
    #                                                 viewonly=True
    #                                                 )
    # livros_lerei = relationship("Livro", 
    #                                                 secondary='join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
    #                                                 # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
    #                                                 # ,
    #                                                 ,primaryjoin="and_(StatusUsuarioLivro.status=='Lerei')"
    #                                                 # secondaryjoin="UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status"
    #                                                 ,uselist=True,
    #                                                 viewonly=True
    #                                                 )
    # livros_lendo = relationship("Livro", 
    #                                                 secondary='join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
    #                                                 # 'join(UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status)'
    #                                                 # ,
    #                                                 ,primaryjoin="and_(StatusUsuarioLivro.status=='Lendo')"
    #                                                 # secondaryjoin="UsuarioLivro, StatusUsuarioLivro, StatusUsuarioLivro.id == UsuarioLivro.fk_status"
    #                                                 ,uselist=True,
    #                                                 viewonly=True
    #                                                 )
    # usuario_avaliacao = relationship("Avaliacao", back_populates="usuario")
    friends = relationship("Friend", back_populates="user_origin")
    # friends = relationship('Friend', backref='Friend.fk_destino',primaryjoin='User.id==Friend.fk_origin', lazy='dynamic')
    # mensagens = relationship('Mensagem', backref='Mensagem.fk_destino',primaryjoin='Usuario.id==Mensagem.fk_origem', lazy='dynamic')


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(Text)

    users = relationship("User", secondary=user_genre, back_populates="genres")
    # generos = relationship("Livro", back_populates="genero")


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, index=True)

    identified = Column(String(25))

    # livros_lendo = relationship("UsuarioLivro", back_populates="livro_lendo")
    # status_usuario_livro = relationship("StatusUsuarioLivro", 
    #                                     secondary='join(UsuarioLivro, Livro, UsuarioLivro.fk_status == Livro.id)'
    #                                     ,secondaryjoin="UsuarioLivro.fk_status == StatusUsuarioLivro.id"
    #                                     ,uselist=True,
    #                                     viewonly=True
    #                                     )
    # test = relationship("UsuarioLivro", back_populates="test1")
    # test2 = relationship("Autor", 
    #                                                 secondary='join(LivroAutores, Autor, Autor.id == LivroAutores.fk_autor)'
    #                                                 ,uselist=True,
    #                                                 viewonly=True
    #                                                 )
    # usuario = relationship("Usuario", 
    #                                                 secondary='join(UsuarioLivro, Usuario, Usuario.id == UsuarioLivro.fk_usuario)'
    #                                                 ,uselist=True,
    #                                                 viewonly=True
    #                                                 )   
    # avaliacoes = relationship("Avaliacao", back_populates="avaliacao")


class Status(Base):
    __tablename__= 'status'

    id = Column(Integer, primary_key=True, index=True)

    status = Column(String(100))

    # livro_status = relationship('UsuarioLivro', back_populates="status")
    # livros = relationship("UsuarioLivro", back_populates="statuss")  


class UserBook(Base):
    __tablename__ = 'user_book'

    fk_book = Column(ForeignKey("book.id"), primary_key=True)
    fk_user = Column(ForeignKey("user.id"), primary_key=True)
    fk_status = Column(ForeignKey("status.id"))
    date = Column(DateTime)

    # livro_lendo = relationship("Livro", back_populates="livros_lendo")
    # usuario = relationship("Usuario", back_populates="lendoss")
    # statuss = relationship("StatusUsuarioLivro", back_populates="livros")
    # test1 = relationship("Livro", back_populates="test")


class Rate(Base):
    __tablename__ = 'rate'

    id = Column(Integer, primary_key=True, index=True)

    text = Column(Text)
    date = Column(DateTime)
    rate = Column(Integer)
    likes = Column(Integer)

    fk_user = Column(ForeignKey("user.id"))
    fk_book = Column(ForeignKey("book.id"))
    fk_like = Column(ForeignKey("like.id"))

    # avaliacao = relationship("Livro", back_populates="avaliacoes")
    # usuario = relationship("Usuario", back_populates="usuario_avaliacao")
    # comentarios = relationship("Likes", back_populates="avaliacao")


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, index=True)    

    text = Column(Text)
    date = Column(DateTime)
    likes = Column(Integer)

    fk_user = Column(ForeignKey("user.id"))
    fk_book = Column(ForeignKey("book.id"))
    fk_rate = Column(ForeignKey("rate.id"))

    # avaliacoes = relationship("Likes", back_populates="comentario")


class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True, index=True)

    fk_comment = Column(ForeignKey("comment.id"))
    fk_rate = Column(ForeignKey("rate.id"))
    fk_user = Column(ForeignKey("user.id"))

    # avaliacao = relationship("Avaliacao", back_populates="comentarios")
    # comentario = relationship("Comentario", back_populates="avaliacoes")


class Friend(Base):
    __tablename__ = 'friend'

    pending = Column(Boolean)
    ignored = Column(Boolean)
    fk_origin = Column(ForeignKey("user.id"), primary_key=True)
    fk_destiny = Column(ForeignKey("user.id"), primary_key=True)

    # user_origin = relationship("User", foreign_keys='Friend.fk_origin')
    # user_destiny = relationship("User", foreign_keys='Friend.fk_destiny')


# class Message(Base):
#     __tablename__ = 'message'

#     id = Column(Integer, primary_key=True, index=True)

#     text = Column(T, nullable=False)
#     date = Column(DateTime)

#     # fk_origin = Column(ForeignKey("user.id"))
#     # fk_destiny = Column(ForeignKey("user.id"))

#     # usuario_origem = relationship("Usuario", foreign_keys='Mensagem.fk_origem')
#     # usuario_destino = relationship("Usuario", foreign_keys='Mensagem.fk_destino')
