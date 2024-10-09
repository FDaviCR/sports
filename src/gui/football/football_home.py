import tkinter as tk
from tkinter import ttk
#from src.gui.football.leagues_screen import Leagues

cor_de_fundo = "gray"

class HomeFootball(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#000000")
        
        subcontainer1 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        subcontainer2 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        subcontainer3 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        subcontainer4 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer4.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        subcontainer5 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer5.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        subcontainer6 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer6.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        subcontainer7 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer7.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        subcontainer8 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer8.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        subcontainer9 = tk.Frame(self, bg=cor_de_fundo)
        subcontainer9.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        # Adicionando labels para identificação em cada subcontainer
        tk.Button(subcontainer1, text="Atualizar Ligas", width=50).pack(pady=20)
        tk.Button(subcontainer1, text="Listar Ligas", width=50).pack(pady=0)
        tk.Label(subcontainer1, text="Data de Atualização: ").pack(expand=True)
        
        tk.Label(subcontainer2, text="Row 0, Col 1").pack(expand=True)
        tk.Label(subcontainer3, text="Row 0, Col 2").pack(expand=True)

        tk.Label(subcontainer4, text="Row 1, Col 0").pack(expand=True)
        tk.Label(subcontainer5, text="Row 1, Col 1").pack(expand=True)
        tk.Label(subcontainer6, text="Row 1, Col 2").pack(expand=True)

        tk.Label(subcontainer7, text="Row 2, Col 0").pack(expand=True)
        tk.Label(subcontainer8, text="Row 2, Col 1").pack(expand=True)
        tk.Label(subcontainer9, text="Row 2, Col 2").pack(expand=True)

        # Configuração para expandir as colunas e linhas do grid igualmente
        for i in range(3):
            self.grid_columnconfigure(i, weight=1, uniform="equal")
            self.grid_rowconfigure(i, weight=1, uniform="equal")



