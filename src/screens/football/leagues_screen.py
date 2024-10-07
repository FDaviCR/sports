import tkinter as tk
from tkinter import ttk

class Leagues(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#2f2f2f")
        label = ttk.Label(self, text="TELA DE LEAGUES", font=("Helvetica", 24))
        label.pack(pady=20, padx=20)

        # Botão para ir para a Tela 2
        botao_ir_tela2 = ttk.Button(self, text="Ir para a Tela 3",
                                    command=lambda: controller.mostrar_tela())
        botao_ir_tela2.pack(pady=10)
