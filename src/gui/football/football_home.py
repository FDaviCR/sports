import tkinter as tk
from tkinter import ttk

from src.functions.general.timezone import createTimezones
from src.functions.general.countries import createCountries

cor_de_fundo = "#454544"

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
        tk.Label(subcontainer1, text="Timezones", width=50, bg=cor_de_fundo, font=("Arial", 20), fg="white").pack(pady=0)
        tk.Button(subcontainer1, text="Listar Timezones", width=50, relief="solid", bd=2).pack(pady=5)
        tk.Button(subcontainer1, text="Atualizar Timezones", width=50, relief="solid", bd=2).pack(pady=5)
        
        tk.Label(subcontainer2, text="Countries", width=50, bg=cor_de_fundo, font=("Arial", 20), fg="white").pack(pady=0)
        tk.Button(subcontainer2, text="Listar Countries", width=50, relief="solid", bd=2).pack(pady=5)
        tk.Button(subcontainer2, text="Atualizar Countries", width=50, relief="solid", bd=2).pack(pady=5)
        
        tk.Label(subcontainer3, text="Em desenvolvimento").pack(expand=True)

        tk.Label(subcontainer4, text="Em desenvolvimento").pack(expand=True)
        tk.Label(subcontainer5, text="Em desenvolvimento").pack(expand=True)
        tk.Label(subcontainer6, text="Em desenvolvimento").pack(expand=True)

        tk.Label(subcontainer7, text="Em desenvolvimento").pack(expand=True)
        tk.Label(subcontainer8, text="Em desenvolvimento").pack(expand=True)
        tk.Label(subcontainer9, text="Em desenvolvimento").pack(expand=True)

        # Configuração para expandir as colunas e linhas do grid igualmente
        for i in range(3):
            self.grid_columnconfigure(i, weight=1, uniform="equal")
            self.grid_rowconfigure(i, weight=1, uniform="equal")



