from sqlalchemy import func, Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import column_property

from src.db.database import Base


class UserGenre(Base):
    __tablename__ = 'user_genre'

    fk_genre = Column(ForeignKey("genre.id"), primary_key=True)
    fk_user = Column(ForeignKey("user.id"), primary_key=True)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(255), unique=True)
    name = Column(String(255))
    nickname = Column(String(30), unique=True)
    description = Column(Text)
    password = Column(String(256))
    photo = Column(String(255), nullable=True)
    code_otp = Column(String(6), nullable=True)
    code_otp_time = Column(DateTime)


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(Text)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String(25))


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(100))


class UserBook(Base):
    __tablename__ = 'user_book'

    fk_book = Column(ForeignKey("book.id"), primary_key=True)
    fk_user = Column(ForeignKey("user.id"), primary_key=True)
    fk_status = Column(ForeignKey("status.id"))
    date = Column(DateTime)
    formatted_date = column_property(func.to_char(date, 'DD/MM/YYYY HH:MM'))


class Rate(Base):
    __tablename__ = 'rate'

    id = Column(Integer, primary_key=True, index=True)

    text = Column(Text)
    date = Column(DateTime)
    rate = Column(Integer)
    likes = Column(Integer)

    fk_user = Column(ForeignKey("user.id"))
    fk_book = Column(ForeignKey("book.id"))

    formatted_date = column_property(func.to_char(date, 'DD/MM/YYYY HH:MM'))


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, index=True)

    text = Column(Text)
    date = Column(DateTime)
    likes = Column(Integer)

    fk_user = Column(ForeignKey("user.id"))
    fk_rate = Column(ForeignKey("rate.id"))

    formatted_date = column_property(func.to_char(date, 'DD/MM/YYYY HH:MM'))


class Like(Base):
    __tablename__ = 'like'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    formatted_date = column_property(func.to_char(date, 'DD/MM/YYYY HH:MM'))
    
    fk_comment = Column(ForeignKey("comment.id"))
    fk_rate = Column(ForeignKey("rate.id"))
    fk_user = Column(ForeignKey("user.id"))


class Friend(Base):
    __tablename__ = 'friend'

    date = Column(DateTime)
    pending = Column(Boolean)
    ignored = Column(Boolean)
    formatted_date = column_property(func.to_char(date, 'DD/MM/YYYY HH:MM'))

    fk_origin = Column(ForeignKey("user.id"), primary_key=True)
    fk_destiny = Column(ForeignKey("user.id"), primary_key=True)

# class Message(Base):
#     __tablename__ = 'message'

#     id = Column(Integer, primary_key=True, index=True)

#     text = Column(T, nullable=False)
#     date = Column(DateTime)

#     # fk_origin = Column(ForeignKey("user.id"))
#     # fk_destiny = Column(ForeignKey("user.id"))

