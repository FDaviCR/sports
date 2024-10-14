import tkinter as tk
from src.functions.general.timezone import createTimezones
from src.functions.general.countries import createCountries

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#010101")

        # Botões para navegar entre as páginas
        button1 = tk.Button(self, 
                            text="Ir para Página de Futebol",
                            command=lambda: controller.show_frame("Page1"), 
                            font=("Helvetica", 14, "bold"),
                            bg="#010101",
                            fg="white",
                            borderwidth=5,
                            cursor="hand2"
        )
        
        button1.pack(side="top", fill="both", expand=True)

        button2 = tk.Button(self, 
                            text="Test", 
                            command=lambda: createCountries(),
                            font=("Helvetica", 14, "bold"),
                            bg="#010101",
                            fg="white",
                            borderwidth=5,
                            cursor="hand2",
                            state="disabled"
        )
        button2.pack(side="top", fill="both", expand=True)

        button3 = tk.Button(self, 
                            text="Ir para Página 3", 
                            command=lambda: controller.show_frame("Page3"),
                            font=("Helvetica", 14, "bold"),
                            bg="#010101",
                            fg="white",
                            borderwidth=5,
                            cursor="hand2",
                            state="disabled"
        )
        button3.pack(side="top", fill="both", expand=True)
