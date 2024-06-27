from app import app, templates  # Importa a instância do FastAPI e o motor de templates.
from fastapi import Form, HTTPException, Request, Depends  # Importa classes e métodos necessários para lidar com formulários, exceções HTTP, requisições e dependências.
from fastapi.responses import HTMLResponse, RedirectResponse  # Importa respostas HTML e redirecionamento.

from sqlalchemy.orm import Session  # Importa a sessão do SQLAlchemy para gerenciar a comunicação com o banco de dados.
from app.database.db import get_db  # Importa a função para obter a sessão do banco de dados.
from app.schemas import biblioteca_schema  # Importa esquemas usados para validação e criação de instâncias.
from app.services import crud_service  # Importa o serviço CRUD para operações no banco de dados.

# Rota principal para exibir a página inicial.
@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    try:
        return templates.TemplateResponse('home.html', {"request": request})  # Renderiza o template 'home.html'.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Levanta uma exceção HTTP 500 em caso de erro.

# Rota para exibir a página de gerenciamento de livros.
@app.get('/book', response_class=HTMLResponse)
async def book_page(request: Request, db: Session = Depends(get_db)):
    try:
        get_author_data = crud_service.get_authors(db)  # Obtém dados dos autores.
        get_book_data = crud_service.get_books(db)  # Obtém dados dos livros.
        return templates.TemplateResponse('livros/home_livro.html', {"request": request, "author_data": get_author_data, "book_data": get_book_data})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Levanta uma exceção HTTP 500 em caso de erro.

# Rota para registrar um novo livro.
@app.post('/book_register', response_class=HTMLResponse)
async def book_register(request: Request, db: Session = Depends(get_db), titulo: str = Form(...), editora: str = Form(...), idioma: str = Form(...), sinopse: str = Form(None), autor: int = Form(...)):
    try:
        book_data = biblioteca_schema.LivroCreate(
            titulo=titulo,
            editora=editora,
            idioma=idioma,
            sinopse=sinopse,
            autor_id=autor
        )
        
        new_book = crud_service.create_book(db, book_data)  # Cria um novo livro no banco de dados.

        if new_book:
            return RedirectResponse('/book', 303)  # Redireciona para a página de gerenciamento de livros após o registro.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Levanta uma exceção HTTP 500 em caso de erro.

# Rota para exibir a página de gerenciamento de autores.
@app.get('/author', response_class=HTMLResponse)
async def author_page(request: Request):
    try:
        return templates.TemplateResponse('autor/home_autor.html', {"request": request})  # Renderiza o template 'home_autor.html'.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Levanta uma exceção HTTP 500 em caso de erro.

# Rota para registrar um novo autor.
@app.post('/author_register', response_class=HTMLResponse)
async def author_register(request: Request, db: Session = Depends(get_db), autor: str = Form(...)):
    try:
        autor_data = biblioteca_schema.AutorCreate(nome=autor)
        new_autor = crud_service.create_author(db, autor_data)  # Cria um novo autor no banco de dados.

        return RedirectResponse('/book', 303)  # Redireciona para a página de gerenciamento de livros após o registro do autor.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Levanta uma exceção HTTP 500 em caso de erro.

# Rota para exibir a página de edição de um livro.
@app.get('/book_edit', response_class=HTMLResponse)
async def book_edit_page(request: Request, id_value: int, db: Session = Depends(get_db)):
    try:
        book = crud_service.get_book(db, id_value)  # Obtém o livro pelo ID.
        if not book:
            return templates.TemplateResponse('404.html', {"request": request, "message": "Livro não encontrado"})  # Renderiza uma página 404 se o livro não for encontrado.
        
        authors = crud_service.get_authors(db)  # Obtém todos os autores para a seleção.

        return templates.TemplateResponse('livros/edit_livro.html', {"request": request, "book": book, "author_data": authors})  # Renderiza a página de edição do livro.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Levanta uma exceção HTTP 500 em caso de erro.

# Rota para atualizar os dados de um livro.
@app.post('/book_edit', response_class=HTMLResponse)
async def book_edit(request: Request, db: Session = Depends(get_db), id_value: int = Form(...), titulo: str = Form(...), editora: str = Form(...), idioma: str = Form(...), sinopse: str = Form(None), autor: int = Form(...)):
    try:
        get_book_data = crud_service.get_book(db, id_value)  # Obtém o livro pelo ID.

        if get_book_data:
            updated_book = crud_service.update_book(db, id_value, titulo, editora, idioma, sinopse, autor)  # Atualiza os dados do livro.
            return RedirectResponse('/book', 303)  # Redireciona para a página de gerenciamento de livros após a atualização.
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Levanta uma exceção HTTP 500 em caso de erro.

# Rota para excluir um livro pelo ID.
@app.post('/delete_book', response_class=HTMLResponse)
async def delete_book(request: Request, db: Session = Depends(get_db), book_id: int = Form(...)):
    try:
        delete_book = crud_service.delete_book(db, book_id)  # Exclui o livro pelo ID.

        if delete_book:
            return RedirectResponse('/book', 303)  # Redireciona para a página de gerenciamento de livros após a exclusão.
        else:
            raise HTTPException(400, "Falha ao excluir o livro. Verifique o id fornecido.")  # Levanta uma exceção HTTP 400 se a exclusão falhar.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  # Levanta uma exceção HTTP 500 em caso de erro.
