# Sistema de Biblioteca - API de Cadastro de Livros

Este é o README do projeto de API web **Sistema de Biblioteca**, desenvolvido para a disciplina de Programação WEB.

## Funcionalidades

- **Cadastro de Livros**: Permite o cadastro de novos livros na base de dados.
- **Deletar Livros**: Permite a exclusão de livros cadastrados.
- **Editar Livros**: Permite a atualização das informações dos livros.
- **Cadastro de Autor**: Implementa a funcionalidade de cadastro de novos autores.

## Requisitos

- **Python e SQLAlchemy**: O projeto é inteiramente implementado utilizando Python e SQLAlchemy para a manipulação do banco de dados.
- **Banco de Dados**: Utiliza SQLite como banco de dados relacional.
- **Interface Web**: Utiliza HTML (Jinja2 templates) e CSS com TailwindCSS para a interface visual.

## Uso da API

### Endpoints Principais

- **GET /**
  - Retorna a página inicial da aplicação.

- **GET /book**
  - Exibe a página de gerenciamento de livros, listando todos os livros e autores.

- **POST /book_register**
  - Cadastro de novos livros.
  - **Parâmetros**: `titulo`, `editora`, `idioma`, `sinopse`, `autor`.
  - **Exemplo**:
    ```json
    {
      "titulo": "O Livro da Alegria",
      "editora": "Editora XYZ",
      "idioma": "Português",
      "sinopse": "Uma conversa inspiradora entre o Dalai Lama e Desmond Tutu.",
      "autor": 1
    }
    ```

- **GET /author**
  - Exibe a página de gerenciamento de autores.

- **POST /author_register**
  - Cadastro de novos autores.
  - **Parâmetros**: `autor` (nome do autor).
  - **Exemplo**:
    ```json
    {
      "autor": "Dalai Lama"
    }
    ```

- **GET /book_edit**
  - Exibe a página de edição de um livro específico.
  - **Parâmetros**: `id_value` (ID do livro).
  - **Exemplo**: `/book_edit?id_value=1`

- **POST /book_edit**
  - Atualiza as informações de um livro específico.
  - **Parâmetros**: `id_value`, `titulo`, `editora`, `idioma`, `sinopse`, `autor`.
  - **Exemplo**:
    ```json
    {
      "id_value": 1,
      "titulo": "O Livro da Alegria - Edição Revisada",
      "editora": "Editora ABC",
      "idioma": "Português",
      "sinopse": "Uma conversa ainda mais inspiradora entre o Dalai Lama e Desmond Tutu.",
      "autor": 1
    }
    ```

- **POST /delete_book**
  - Deleta um livro com base no ID fornecido.
  - **Parâmetros**: `book_id` (ID do livro).
  - **Exemplo**:
    ```json
    {
      "book_id": 1
    }
    ```

## Instalação

### Requisitos Pré-Requisitos

- **Python 3**: Assegure-se de ter o Python 3 instalado em seu sistema.

### Passo a Passo de Instalação

1. **Clone o projeto**

   ```bash
   git clone https://github.com/
   ```

2. **Crie um ambiente virtual**

   ```bash
   pip install virtualenv
   virtualenv venv
   ```

3. **Ative o ambiente virtual e instale as dependências**

   ```bash
   # No Windows
   venv\Scripts\activate
   pip install -r requirements.txt

   # No Linux/MacOS
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configurar variáveis de ambiente**

   - Crie um arquivo `.env` na raiz do projeto e adicione a variável de ambiente `SQLALCHEMY_DATABASE_URL` com o caminho do seu banco de dados SQLite ou outro de sua preferência.
     ```plaintext
     SQLALCHEMY_DATABASE_URL=sqlite:///./test.db
     ```

5. **Inicie o servidor**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Acesse a aplicação**

   - Abra o navegador e vá para `http://127.0.0.1:8000/` para acessar a interface da aplicação.

## Estrutura de Pastas

- **/app**: Diretório principal contendo os módulos da aplicação.
  - **/templates**: Diretório contendo os arquivos HTML da interface.
  - **/static**: Diretório contendo arquivos estáticos como CSS e imagens.
  - **/database**: Contém a configuração do banco de dados.
  - **/schemas**: Define os esquemas utilizados para validação de dados.
  - **/services**: Contém os serviços de CRUD (Create, Read, Update, Delete).
  - **main.py**: Arquivo principal para iniciar a aplicação.

---
