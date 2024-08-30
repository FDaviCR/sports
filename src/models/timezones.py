from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

host=os.getenv('MYSQL_HOST')
user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')
database=os.getenv('MYSQL_DATABASE')

# Configuração do banco de dados MySQL
DATABASE_URL = "mysql+mysqlconnector://"+ user +":" + password + "@"+ host +"/"+ database

# Criando a engine de conexão com o MySQL
engine = create_engine(DATABASE_URL)

# Base para os modelos de dados
Base = declarative_base()

# Definição do modelo de dados para a tabela de usuários
class Timezone(Base):
    __tablename__ = 'timezones'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    timezone = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Timezone(timezone='{self.timezone}')>"

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Exemplo de como adicionar um novo usuário ao banco de dados
new_tz = Timezone(timezone="test/TS")
session.add(new_tz)
session.commit()

# Exemplo de como consultar usuários
timezones = session.query(Timezone).all()
for timezone in timezones:
    print(timezone)
