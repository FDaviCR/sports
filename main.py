import tkinter as tk
import src.gui.home as HomePage
import src.gui.football.football_home as HomeFootball
#from page2 import Page2
#from page3 import Page3

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sports")
        self.state('zoomed')
        
        # Container para segurar as páginas
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dicionário para armazenar as páginas
        self.frames = {}

        # Adicionando as páginas ao dicionário
        for F in (HomePage.HomePage, HomeFootball.HomeFootball):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Mostra a página de acordo com o nome fornecido'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
