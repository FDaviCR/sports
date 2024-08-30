from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error


load_dotenv()

def conectar():
    try:
        # Configurações de conexão
        conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )

        if conn.is_connected():
            print('Conexão com o MySQL estabelecida com sucesso!')
            return conn

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def urlDatabase():
    host=os.getenv('MYSQL_HOST')
    user=os.getenv('MYSQL_USER')
    password=os.getenv('MYSQL_PASSWORD')
    database=os.getenv('MYSQL_DATABASE')
    
    DATABASE_URL = "mysql+mysqlconnector://"+ user +":" + password + "@"+ host +"/"+ database

    return DATABASE_URL