import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        # Configurações de conexão
        conn = mysql.connector.connect(
            host='localhost',
            user='seu_usuario',
            password='sua_senha',
            database='nome_do_banco_de_dados'
        )

        if conn.is_connected():
            print('Conexão com o MySQL estabelecida com sucesso!')
            return conn

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
