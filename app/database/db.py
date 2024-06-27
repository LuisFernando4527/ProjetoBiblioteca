from os import environ
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Carrega variáveis de ambiente a partir de um arquivo `.env`.
load_dotenv()

# Obtém a URL do banco de dados a partir das variáveis de ambiente.
# Espera-se que a variável "SQLALCHEMY_DATABASE_URL" esteja definida no arquivo `.env` ou no ambiente.
DATABASE_URL = environ.get("SQLALCHEMY_DATABASE_URL")

# Verifica se a URL do banco de dados foi encontrada. Caso contrário, levanta um erro.
if not DATABASE_URL:
    raise ValueError("Não foi encontrado variavel com o nome especificado.")

# Cria a engine do SQLAlchemy com base na URL do banco de dados.
# `connect_args={"check_same_thread": False}` é específico para o SQLite e permite conexões em múltiplas threads.
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Configura o `sessionmaker` para criar novas sessões com a engine criada.
# `autoflush=False` impede o envio automático de mudanças ao banco de dados antes de uma chamada explícita ao `commit`.
SessionLocal = sessionmaker(autoflush=False, bind=engine)

# Cria uma classe base para os modelos ORM a partir do `declarative_base` do SQLAlchemy.
Base = declarative_base()

# Função geradora `get_db` para obter uma sessão do banco de dados.
# Garante que a sessão será fechada após o uso.
def get_db():
    db = SessionLocal()  # Cria uma nova sessão do banco de dados.
    try:
        yield db  # Fornece a sessão para ser usada em um bloco `with` ou em uma dependência do FastAPI.
    finally:
        db.close()  # Garante que a sessão será fechada ao finalizar o uso, liberando recursos.