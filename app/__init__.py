from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from .database.db import engine, Base

load_dotenv()

# Configuração do banco de dados
Base.metadata.create_all(bind=engine)

# Instanciação do FastAPI
app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key='secret_key')

# Configuração de arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configuração de templates com JINJA2
templates = Jinja2Templates(directory="app/templates")

from app.views import routes