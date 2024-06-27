from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.db import Base

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    data_criacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    books = relationship('Livro', back_populates='author')

class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False, index=True)
    editora = Column(String, nullable=False)
    idioma = Column(String, nullable=False)
    sinopse = Column(String, nullable=True)
    data_criacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')