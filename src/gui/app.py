import tkinter as tk
from src.gui.home_screen import Home
from src.gui.football.leagues_screen import Leagues

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sports")
        self.state('zoomed')  # Janela maximizada

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, Leagues):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(Home)

    def mostrar_tela(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
