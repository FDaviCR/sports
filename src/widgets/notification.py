
import tkinter as tk
from tkinter import Toplevel
import threading

import src.functions.general.timezone as tz

# Função a ser executada (simulação com delay)
def long_running_task():
    try:
        tz.createTimezones()
        popup.destroy()  # Fecha o popup ao finalizar
    except:
        popup.destroy()
        popupErro = Toplevel()
        popupErro.title("Erro...")
        tk.Label(popupErro, text="Aconteceu um erro...").pack(pady=100, padx=100)
        

# Função que cria o popup e executa a tarefa em uma thread
def start_task_with_popup():
    global popup
    # Criando o popup
    popup = Toplevel()
    popup.title("Aguarde...")
    tk.Label(popup, text="Processando...").pack(pady=100, padx=100)
    
    # Criar e iniciar uma thread para executar a função
    task_thread = threading.Thread(target=long_running_task)
    task_thread.start()
