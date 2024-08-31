import mysql.connector
from mysql.connector import Error

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL, MYSQL_HOST, MYSQL_DATABASE, MYSQL_PASSWORD, MYSQL_USER

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    import models.timezones  
    Base.metadata.create_all(bind=engine)

def conectar():
    try:
        conn = mysql.connector.connect(
            MYSQL_HOST,
            MYSQL_USER,
            MYSQL_PASSWORD,
            MYSQL_DATABASE
        )

        if conn.is_connected():
            print('Conexão com o MySQL estabelecida com sucesso!')
            return conn

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
