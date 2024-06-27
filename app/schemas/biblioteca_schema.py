# schemas/author.py
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class AutorBase(BaseModel):
    """
    Esquema básico para representar um autor.
    """
    nome: str

    class Config:
        from_attributes = True

class AutorCreate(AutorBase):
    pass

class Autor(AutorBase):
    id: int
    user_id: int
    data_criacao: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True

class LivroBase(BaseModel):
    """
    Classe base para representar os dados básicos de um livro.
    """
    titulo: str
    editora: Optional[str] = None
    idioma: Optional[str] = None
    sinopse: Optional[str] = None

class LivroCreate(LivroBase):
    """
    Classe para representar os dados necessários para criar um novo livro.
    """
    autor_id: int

class LivroUpdate(LivroBase):
    pass

class Livro(LivroBase):
    """
    Classe para representar um livro completo.
    """
    id: int
    autor_id: int
    data_criacao: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True

