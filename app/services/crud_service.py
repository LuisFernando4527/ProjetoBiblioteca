from sqlalchemy.orm import Session, joinedload  # Importa `Session` para gerenciar a conexão com o banco de dados e `joinedload` para carregar relacionamentos.
from ..models.Model import Author, Livro  # Importa os modelos `Author` e `Livro` da aplicação.
from ..schemas.biblioteca_schema import AutorCreate, LivroCreate  # Importa os esquemas `AutorCreate` e `LivroCreate` da aplicação.

# Função para obter um autor específico pelo seu ID.
def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

# Função para obter uma lista de autores com a possibilidade de pular (skip) os primeiros e limitar o número de resultados (limit).
def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()

# Função para criar um novo autor.
# Recebe um objeto `AutorCreate` com os dados do novo autor.
def create_author(db: Session, author: AutorCreate):
    db_author = Author(name=author.nome)  # Cria uma instância de `Author` com o nome fornecido.
    db.add(db_author)  # Adiciona o novo autor à sessão.
    db.commit()  # Envia a transação para o banco de dados.
    db.refresh(db_author)  # Atualiza o objeto `db_author` com os dados do banco de dados.
    return db_author  # Retorna o autor criado.

# Função para atualizar o nome de um autor existente.
def update_author(db: Session, author_id: int, nome: str):
    db_author = db.query(Author).filter(Author.id == author_id).first()  # Obtém o autor pelo ID.
    if db_author:  # Verifica se o autor foi encontrado.
        db_author.name = nome  # Atualiza o nome do autor.
        db.commit()  # Envia a transação para o banco de dados.
        db.refresh(db_author)  # Atualiza o objeto `db_author` com os dados do banco de dados.
    return db_author  # Retorna o autor atualizado.

# Função para excluir um autor pelo seu ID.
# Retorna `True` se a exclusão for bem-sucedida e `False` caso contrário.
def delete_author(db: Session, author_id: int) -> bool:
    db_author = db.query(Author).filter(Author.id == author_id).first()  # Obtém o autor pelo ID.
    if db_author:  # Verifica se o autor foi encontrado.
        db.delete(db_author)  # Remove o autor da sessão.
        db.commit()  # Envia a transação para o banco de dados.
        return True  # Retorna `True` indicando sucesso.
    return False  # Retorna `False` se o autor não foi encontrado.

# Função para obter um livro específico pelo seu ID.
def get_book(db: Session, book_id: int):
    return db.query(Livro).filter(Livro.id == book_id).first()

# Função para obter uma lista de livros com a possibilidade de pular (skip) os primeiros e limitar o número de resultados (limit).
# Usa `joinedload` para carregar os dados do autor junto com os livros.
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Livro).options(joinedload(Livro.author)).offset(skip).limit(limit).all()

# Função para criar um novo livro.
# Recebe um objeto `LivroCreate` com os dados do novo livro.
def create_book(db: Session, book: LivroCreate):
    db_book = Livro(
        titulo=book.titulo,
        editora=book.editora,
        idioma=book.idioma,
        sinopse=book.sinopse,
        author_id=book.autor_id  # Associa o livro ao autor usando o `autor_id`.
    )
    db.add(db_book)  # Adiciona o novo livro à sessão.
    db.commit()  # Envia a transação para o banco de dados.
    db.refresh(db_book)  # Atualiza o objeto `db_book` com os dados do banco de dados.
    return db_book  # Retorna o livro criado.

# Função para atualizar os dados de um livro existente.
# Atualiza título, editora, idioma, sinopse e o autor associado.
def update_book(db: Session, book_id: int, titulo: str, editora: str, idioma: str, sinopse: str, autor_id: int):
    db_book = db.query(Livro).filter(Livro.id == book_id).first()  # Obtém o livro pelo ID.
    if db_book:  # Verifica se o livro foi encontrado.
        db_book.titulo = titulo  # Atualiza o título do livro.
        db_book.editora = editora  # Atualiza a editora do livro.
        db_book.idioma = idioma  # Atualiza o idioma do livro.
        db_book.sinopse = sinopse  # Atualiza a sinopse do livro.
        db_book.author_id = autor_id  # Atualiza o autor associado ao livro.
        db.commit()  # Envia a transação para o banco de dados.
        db.refresh(db_book)  # Atualiza o objeto `db_book` com os dados do banco de dados.
    return db_book  # Retorna o livro atualizado.

# Função para excluir um livro pelo seu ID.
# Retorna `True` se a exclusão for bem-sucedida e `False` caso contrário.
def delete_book(db: Session, book_id: int) -> bool:
    db_book = db.query(Livro).filter(Livro.id == book_id).first()  # Obtém o livro pelo ID.
    if db_book:  # Verifica se o livro foi encontrado.
        db.delete(db_book)  # Remove o livro da sessão.
        db.commit()  # Envia a transação para o banco de dados.
        return True  # Retorna `True` indicando sucesso.
    return False  # Retorna `False` se o livro não foi encontrado.
