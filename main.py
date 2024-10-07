import tkinter as tk
from src.screens.home_screen import Home
from src.screens.football.leagues_screen import Leagues

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sports")

        # Definir o tamanho máximo da tela
        self.state('zoomed')  # Janela maximizada

        # Container que vai armazenar as telas
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.configure(background='black')

        # Dicionário que vai armazenar as instâncias das telas
        self.frames = {}

        # Instanciar e adicionar as telas ao container
        for F in (Home, Leagues):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostrar a primeira tela no início
        self.mostrar_tela(Home)

    def mostrar_tela(self, cont):
        # Eleva a tela solicitada (raise) no container
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
