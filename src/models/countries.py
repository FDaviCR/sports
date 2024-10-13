from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

# Configuração do banco de dados MySQL
DATABASE_URL = os.getenv('DATABASE_URL')

# Criando a engine de conexão com o MySQL
engine = create_engine(DATABASE_URL)

# Base para os modelos de dados
Base = declarative_base()

# Definição do modelo de dados para a tabela de usuários
class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    code = Column(String(10), nullable=False, unique=True)
    flag = Column(String(500), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Country(name='{self.name}')>"

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()
